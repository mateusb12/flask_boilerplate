
# Flask Backend Boilerplate Documentation


![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-blue.svg)

## 🚀 Introduction

Welcome to **Flask Backend Boilerplate**! This project is a robust and scalable web application built with Flask, designed to handle complex business logic, secure authentication, and efficient database interactions. Whether you're a developer looking to contribute or a user aiming to understand the architecture, this README provides a comprehensive overview to get you started.

## 📋 Table of Contents

- [🚀 Introduction](#-introduction)
- [✨ Features](#-features)
- [📄 Documentation](#-documentation)
- [⚙️ Installation](#-installation)
- [🛠️ Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## ✨ Features

- **User Authentication**: Secure login and registration with JWT.
- **Business Logic Layer**: Organized utilities and exception handling.
- **Database Management**: SQLAlchemy integration with PostgreSQL.
- **Error Handling**: Custom exception classes and error handlers.
- **API Documentation**: Swagger integration for API endpoints.
- **CORS Support**: Configurable Cross-Origin Resource Sharing.
- **SocketIO Integration**: Real-time communication capabilities.

## 📄 Documentation
### Key modules
- `app_instance_creation.py`:  Initializes the Flask application, configures the database, JWT, and CORS
- `populator.py`: Populates the database with initial data
- `core_instances.py`: Creates instances for the Flask app, Swagger API, and SocketIO
- `user_model.py`: Defines the `SystemUser` model with methods for password management and database operations.
- `auth_endpoints.py`: Handles authentication routes like login, registration, token refresh, and logout.
- `jwt_error_handlers.py`: Handles JWT errors, including invalid token, expired token, and missing token.

### Exception handling
- Custom exceptions are defined in `dto_custom_exceptions.py` and handled globally via `flask_error_handlers.py`. This ensures consistent error responses across the application.

### Database models
- Located in the `models/database_entities` directory, the database models define the structure and relationships of the application's data.

### Utilities
- The `business_logic/utils` directory contains utility modules for environment management, exception handling, and Flask-specific utilities.

## ⚙️ Installation

Follow these steps to set up the project locally.

1. Clone the repository
```bash
git clone https://github.com/yourusername/your-project-name.git
cd your-project-name
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
- Create a .env file in the root directory and add the following variables:
```dotenv
POSTGRES_DB_NAME=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
JWT_SECRET_KEY=your_jwt_secret_key
```

## 🛠️ Usage

### Running the application

```bash
python app.py
```
- The application will be available at http://localhost:5000

## 📡 API Endpoints

- Authentication
- - `POST /auth/login`: Login user
- - `POST /auth/register`: Register a new user
- - `POST /auth/refresh_token`: Refresh JWT token
- - `GET /auth/get_user_claims`: Retrieve user claims
- - `POST /auth/logout`: Logout user

- User management
- - `GET /users`: Retrieve all users.
- - `GET /users/<id>`: Retrieve a specific user.


_For detailed API documentation, refer to the [Documentation](#-documentation)._

## 🤝 Contributing

Contributions are welcome! Just create a pull request and you will be fine.

## 📜 License
This project is licensed under the [MIT License](LICENSE)