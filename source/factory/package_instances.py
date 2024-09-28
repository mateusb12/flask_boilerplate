from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db_instance = SQLAlchemy()
jwt_instance = JWTManager()