# Flask Todo App

![Todo App](static/images/MyTodo-logo.png)

## Overview

This is a feature-rich todo application built with Flask, MongoDB, and Flask-PyMongo. The app allows users to manage their tasks efficiently, with functionalities like user authentication, task creation, updating, and deletion. With an intuitive user interface, this app provides a seamless experience for organizing daily tasks.

## Features

- **User Authentication:** Users can sign up, log in, and log out securely.
- **Task Management:** Create, update, and delete tasks with ease.
- **User-specific Tasks:** Each user has their own set of tasks, ensuring privacy and organization.
- **Responsive Design:** The app is designed to work seamlessly on desktop and mobile devices.

## Deployment

The application is deployed on [Render](https://render.com/) and can be accessed at [https://mytodoflaskapp.onrender.com/](https://mytodoflaskapp.onrender.com/).

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory with the following variables:
   ```dotenv
   MONGO_URI=your_mongodb_uri_here
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:5000`.

## Usage

1. **Register/Login:**
   - Register a new account or log in with an existing one.

2. **Manage Tasks:**
   - Create new tasks with titles and descriptions.
   - Update tasks by editing their titles and descriptions.
   - Delete tasks when they are completed or no longer needed.

3. **Log Out:**
   - Securely log out of your account when done.

## Technologies Used

- **Flask:** A lightweight web application framework for Python.
- **MongoDB:** A NoSQL database for storing user data and tasks.
- **Flask-PyMongo:** A Flask extension for interacting with MongoDB.
- **HTML/CSS:** Used for the frontend design and layout.
- **Python:** The programming language used for backend logic.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests for new features, improvements, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the Flask and MongoDB communities for their amazing documentation and support.
- Icons used in the app are from [FontAwesome](https://fontawesome.com/).

---

This README provides a comprehensive overview of the Flask todo app, highlighting its features, installation process, usage instructions, deployment information, and the technologies used. Feel free to customize it further to suit your project's needs.