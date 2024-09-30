from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

print("package_instances.py imported!")

db_instance = SQLAlchemy()
jwt_instance = JWTManager()