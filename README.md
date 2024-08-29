# Blog Post Site

## Project Overview

This is a blog post site built using the Flask web framework. The platform allows users to register, create accounts, and post their own blog entries. It is designed to be user-friendly and secure, making it easy for anyone to share their thoughts and ideas.

## Features

- **User Registration**: New users can sign up with an email and password.
- **User Authentication**: Secure login and logout functionality.
- **Create Posts**: Registered users can create new blog posts.
- **View Posts**: Users can browse all posts created by others.
- **Edit & Delete Posts**: Users can edit or delete their own posts.
- **Responsive Design**: The site is designed to be accessible on both desktop and mobile devices.

## Installation

### Prerequisites

- Python 3.x
- Flask
- PostgreSQL (or any other preferred database)

### Steps to Set Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   - Create a PostgreSQL database and update the database URI in the configuration file.
   - Initialize the database:

     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

5. **Run the Application**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Configuration

The application uses environment variables to manage configurations. Make sure to set up the following variables:

- `SECRET_KEY`: A secret key for session management.
- `SQLALCHEMY_DATABASE_URI`: The database URI to connect to your PostgreSQL database.
- `MAIL_USERNAME` and `MAIL_PASSWORD`: If using email services for account verification.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, please contact:

- **Andrei Saúl Ortega Arzola**
- **Email**: support@androide47.com
- **Company**: Androide47

---

Feel free to customize this template further to suit your specific project needs!