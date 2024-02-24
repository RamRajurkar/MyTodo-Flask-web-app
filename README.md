
---

# Todo App

This is a simple Todo web application built using Flask and MongoDB.

## Features

- **User Authentication:** Users can sign up and log in to manage their todos.
- **CRUD Operations:** Users can create, read, update, and delete todos.
- **Session Management:** Uses session to keep track of logged-in users.
- **Contact Form:** Users can send messages through the contact form.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/RamRajurkar/MyTodo-Flask-web-app.git
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MongoDB URI:**

   - Ensure MongoDB is installed and running on your system.
   - Update the MongoDB URI in `app.py` to match your MongoDB setup:

     ```python
     app.config['MONGO_URI'] = 'mongodb://localhost:27017/Todo_App_Database'
     ```

4. **Run the Flask application:**

   ```bash
   python app.py
   ```

5. **Access the application:**

   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Technologies Used

- **Flask:** Micro web framework for Python.
- **MongoDB:** NoSQL database for storing todo items and user information.
- **HTML/CSS:** Frontend design and styling.
- **JavaScript:** Client-side interactivity and form validation.


## Usage

1. **Sign Up:** Register a new account with a unique username and email address.
2. **Log In:** Use your username and password to log in to the application.
3. **Create Todos:** Add new todos with a title and description.
4. **Update Todos:** Edit existing todos to change their title or description.
5. **Delete Todos:** Remove todos that are no longer needed.
6. **Log Out:** Safely log out of your account when finished.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
