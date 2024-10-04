from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from business_logic.utils.decorator_utils import singleton


@singleton
def get_db_instance():
    return SQLAlchemy()

@singleton
def get_jwt_instance():
    return JWTManager()

print("package_instances.py executed!")