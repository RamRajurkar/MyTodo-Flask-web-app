# from collections import UserDict
from bson import ObjectId
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify, session
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import secrets
from dotenv import load_dotenv
import os
from werkzeug.security import check_password_hash, generate_password_hash


load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/Todo_App_Database'
# app.config['MONGO_URI'] = mongodb_uri = 'mongodb+srv://ramrajurkar2020:ramdb013@cluster0.xwifiky.mongodb.net/Todo_App_Database'

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

current_datetime = datetime.now()

# Format and print the current date and time
datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/', methods=['GET', 'POST'])
def index():

    
    if 'user' in session:
        current_user = session['user']['username']
        user_collection = mongo.db[current_user]

        if request.method == 'POST':
            todo_title = request.form.get('title')
            todo_description = request.form.get('description')

            user_collection.insert_one({'title': todo_title, 'description': todo_description, 'datetime': datetime})

        todos_data = user_collection.find()
        todos_count = user_collection.count_documents({})
        user_details = mongo.db.user_details.find_one({'username': current_user})

        return render_template("index.html", todos=todos_data, todos_count=todos_count, user_details=user_details)
    else:
        return render_template("index.html", todos=None, todos_count=0)

@app.route("/delete/<string:id>")
def delete_todo(id):
    try:
        todo_id = ObjectId(id)
        current_user = session['user']['username']
        user_collection = mongo.db[current_user]
        user_collection.delete_one({"_id": todo_id})
        return redirect(url_for("index"))
    except Exception as e:
        print(f"Error deleting todo: {e}")
        flash("Error deleting todo", "error")
        return redirect(url_for("index"))

@app.route("/update/<string:id>", methods=["GET", "POST"])
def update_todo(id):
    try:
        todo_id = ObjectId(id)
        current_user = session['user']['username']
        user_collection = mongo.db[current_user]
        todo = user_collection.find_one({"_id": todo_id})

        if request.method == "POST":
            user_collection.update_one(
                {"_id": todo_id},
                {"$set": {"title": request.form['title'], "description": request.form['description']}}
            )
            flash("Task Updated Successfully!", "success")
            return redirect(url_for("index"))

        return render_template("update.html", todo=todo)
    except Exception as e:
        print(f"Error updating todo: {e}")
        flash("Error updating todo", "error")
        return redirect(url_for("index"))

existing_usernames = []


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = generate_password_hash(request.form.get('password'))

        user_details = mongo.db.user_details
        user_details.insert_one({'username': username, 'password': password, 'email': email, 'datetime': datetime})

        if check_username_uniqueness(username):
            existing_usernames.append(username)
            session['user'] = {'username': username}
            mongo.db.create_collection(username)
            return redirect(url_for("index"))
        else:
            return jsonify('Username already exists.')
            

    return render_template("sign-in.html")

def check_username_uniqueness(username):
    return username not in existing_usernames

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pswd')

        user_details = mongo.db.user_details
        user_login_details = mongo.db.user_login_details
        user_login_details.insert_one({'username': username, 'logged-in-time': datetime})
        user_data = user_details.find_one({'username': username})

        if user_data and check_password_hash(user_data['password'], password):
            session['user'] = {'username': username}
            return redirect(url_for("index"))
        else:
            # flash('Invalid username or password.', 'error')
            # return render_template("alert.html")
            return jsonify("Invalid Username and password!")

    return render_template("sign-in.html")


@app.route('/logout')
def logout():
    # Clear the user session
    session.pop('user', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template("about-us.html")

@app.route('/contact',  methods= ["GET", "POST"])
def contact():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        message = request.form.get('message')

        user_contact_details = mongo.db.user_contact_details
        user_contact_details.insert_one({'fullname': fullname, 'email': email, 'message': message})
        return jsonify("Your details sent successfully!") 
    return render_template("contactt.html")

if __name__ == "__main__":
    app.run(debug=True)
