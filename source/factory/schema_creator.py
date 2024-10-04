from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, text

from database.populate.populator import populate_pipeline
from factory.central_db_instance import db_instance
from factory.enum_creation import _create_database_enums
from factory.flask_instance import app

def _recreate_database_tables(input_db_instance: SQLAlchemy):
    metadata = MetaData()
    metadata.reflect(input_db_instance.engine)
    metadata.drop_all(input_db_instance.engine)

    # Creating unaccented extension
    with input_db_instance.engine.connect() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))

    _create_database_enums(db_instance)
    input_db_instance.create_all()
    print("Database tables recreated.")

jwt_instance = JWTManager(app)
with app.app_context():
    _recreate_database_tables(db_instance)
    populate_pipeline()


def get_db_instance():
    return db_instance

def get_jwt_instance():
    return jwt_instance