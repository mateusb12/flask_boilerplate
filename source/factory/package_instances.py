from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from business_logic.utils.decorator_utils import singleton


@singleton
def get_db_instance():
    return SQLAlchemy()

jwt_instance = JWTManager()

print("package_instances.py executed!")