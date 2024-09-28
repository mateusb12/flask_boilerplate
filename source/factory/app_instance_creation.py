from os import getenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from sqlalchemy import text

from database.populate.populator import populate_pipeline
from factory.enum_creation import _create_database_enums
from source.factory.package_instances import jwt_instance, db_instance
from source.paths.folder_reference import get_static_folder_path

from source.models.data_transfer_objects.flask_error_handlers import register_error_handlers


def _recreate_database_tables(input_db_instance: SQLAlchemy):
    metadata = MetaData()
    metadata.reflect(input_db_instance.engine)
    metadata.drop_all(input_db_instance.engine)

    # Creating unaccented extension
    with input_db_instance.engine.connect() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))

    _create_database_enums(db_instance)
    input_db_instance.create_all()
    print("Database recreated!")


def _create_postgres_connection_url() -> str:
    db_name = getenv("POSTGRES_DB_NAME")
    db_user = getenv("POSTGRES_USER")
    db_password = getenv("POSTGRES_PASSWORD")
    db_host = getenv("POSTGRES_HOST")
    db_port = getenv("POSTGRES_PORT")
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


def create_flask_app(recreate_db: bool = False) -> Flask:
    # Overall configs
    flask_app = Flask(__name__, static_folder=get_static_folder_path())
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = _create_postgres_connection_url()
    flask_app.config['JWT_SECRET_KEY'] = 'marcelo'
    flask_app.config['FLASK_APP'] = 'app.py'

    # Overall instance connections
    jwt_instance.init_app(flask_app)
    db_instance.init_app(flask_app)
    register_error_handlers(flask_app)

    if recreate_db:
        with flask_app.app_context():
            _recreate_database_tables(db_instance)
    handle_app_cors(flask_app)
    with flask_app.app_context():
        populate_pipeline()
    return flask_app


def handle_app_cors(input_app: Flask):
    cors_url = ['http://localhost:5173', 'http://127.0.0.1:5173']
    CORS(input_app, resources={r"/*": {"origins": cors_url}})

