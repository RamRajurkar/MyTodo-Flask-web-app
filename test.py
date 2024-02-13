# from flask import Flask,render_template,request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# # class Todo(db.Model):
# #     sno = db.Column(db.Integer, primary_key = True)
# #     tittle = db.Column(db.String(200), nullable = False)
# #     desc = db.Column(db.String(500), nullable = False)
# #     date_created = db.Column(db.DateTime, default = datetime.utcnow)

# #     def __repr__(self) -> str:
# #         return f"{self.sno}-{self.tittle}"

# from flask import Flask
# from flask_pymongo import PyMongo

# app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/Todo_App_Database'
# mongo = PyMongo(app)

# # @app.route('/')
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Access the MongoDB collection
#         collection = mongo.db.Todo_list_collection
#         # Retrieve form data
#         Todo_Tittle = request.form.get('tittle')
#         Todo_desc = request.form.get('desc')  # Remove unnecessary float conversion

#         # Insert data into MongoDB
#         collection.insert_one({'tittle': Todo_Tittle, 'desc': Todo_desc})

#         # Redirect to the index page
#         return redirect(url_for('index'))

#     todos = collection.find()
#     for todo in todos:
#         print(todo)
#     # return render_template("index.html", todos=todos)

#     # return render_template("index.html")
#     # return render_template("index.html", todos=todos)



#     # collection = mongo.db.Todo_list_collection
#     # result = collection.find_one({'key': 'value'})
#     # return f"Result from MongoDB: {result}"

# # @app.route('/hello')
# # def hello_world():
# #     # return 'Hello, World!'
# #     return render_template("index.html")

# # @app.route('/products')
# # def products():
# #     return 'These is Products tab'


# if __name__ == "__main__":
#     app.run(debug=True)

#-------------------------------------------------------------------------------------

import pymongo

if __name__ == "__main__":
    # 1. create a connection to MongoDB, with the host as 'localhost' and port
    # Create a connection to the database
    print("Welcome to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['Ram1']
    collection = db['MyCollection']

    # Insertion (Single)
    # dict = {'Name' : 'Ram', 'Marks' : 100}
    # collection.insert_one(dict)

    # dict = {'Name' : 'Shon', 'Marks' : 90}
    # collection.insert_one(dict)

    # dict = {'Name' : 'Pratik', 'Marks' : 80}
    # collection.insert_one(dict)

    # Insertion (Many)
    # dict_list = [
    #     { 'Name': 'Ajay', 'Age': 35},
    #     { 'Name': 'John', 'Age': 45},
    #     { 'Name': 'Ravi', 'Age': 25},
    #     { 'Name': 'kumar', 'Age': 55}
    #      ]
    # collection.insert_many(dict_list)
    # result = collection.insert_many(dict_list, ordered=False)
    # print('Inserted %s records.' % len(result.inserted_ids))
    # # Print all documents in the MyCollection
    # for document in collection.find():
    #     print(document)

    # Find

    # one = collection.find_one()
    # one = collection.find_one({'Name': 'Ram'})
    # print(one)

    # allDocs  = collection.find({'Name': 'Ram'}, {'Name': 1 , '_id': 0}).limit(1)
    allDocs  = collection.find({"Name":"kumar","Age": {"$gte":50}} ,{'Name': 1 })

    # $gte = Greater than
    # $lte = Less than

    for item in allDocs:
        print(item)

    # print(collection.count_documents({}))
    # Update
    # prev = {"Name":"Shon"}
    # nextt = {"$set":{"Marks":"50"}}
    # collection.update_one(prev, nextt)

    # prev = {"Name":"Ajay"}
    # nextt = {"$set":{"Age":"18"}}
    # a = collection.update_many(prev, nextt)
    # print(a.modified_count)

    # prev = {"Name":"Ajay"}
    # nextt = {"$set":{"Age":"111111111111111111111111111"}}
    # collection.update_one(prev, nextt)

    # Delete One
    # doc = {"Name":"Ajay"}
    # collection.delete_one(doc)

    # delete many
    # doc = {"Name":"Ravi"}
    # del_count = collection.delete_many(doc)
    # print(del_count.deleted_count)


    





#---------------------------------------------------------------------------------
        
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Todo_App_Database'
client = MongoClient('mongodb://localhost:27017/')
db = client['Todo_App_Database']
collection = db['Todo_list_collection']
# mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Access the MongoDB collection
    # collection = mongo.db.Todo_list_collection  # Comment out this line

    if request.method == 'POST':
        # Retrieve form data
        key = ""
        Todo_Tittle = request.form.get('tittle')
        Todo_desc = request.form.get('desc')

        # Insert data into MongoDB
        collection.insert_one({'tittle': Todo_Tittle, 'desc': Todo_desc})

        key = collection.find({'tittle': Todo_Tittle, 'desc': Todo_desc })
        return render_template("index.html", key=key)
    else:
        return render_template("index.html")
    # return render_template("index.html", key = key)


@app.route('/products')
def products():
    return 'These are Products tab'

if __name__ == "__main__":
    app.run(debug=True)

