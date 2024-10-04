from os import getenv

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from models.data_transfer_objects.flask_error_handlers import register_error_handlers
from paths.folder_reference import get_static_folder_path


def _create_postgres_connection_url() -> str:
    db_name = getenv("POSTGRES_DB_NAME")
    db_user = getenv("POSTGRES_USER")
    db_password = getenv("POSTGRES_PASSWORD")
    db_host = getenv("POSTGRES_HOST")
    db_port = getenv("POSTGRES_PORT")
    all_data = [db_name, db_user, db_password, db_host, db_port]
    all_tags = ["POSTGRES_DB_NAME", "POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_HOST", "POSTGRES_PORT"]
    for data, tag in zip(all_data, all_tags):
        if not data:
            raise Exception(f"Missing required environment variable: {tag}")
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


def handle_app_cors(input_app: Flask):
    ports = [3000, 5173]
    cors_url = []
    for port in ports:
        cors_url.append(f'http://localhost:{port}')
        cors_url.append(f'http://127.0.0.1:{port}')
    CORS(input_app, resources={r"/*": {"origins": cors_url}})


load_dotenv()
app = Flask(__name__, static_folder=get_static_folder_path())

app.config['SQLALCHEMY_DATABASE_URI'] = _create_postgres_connection_url()
app.config['SQLALCHEMY_ECHO'] = False
app.config['JWT_SECRET_KEY'] = 'marcelo'
app.config['FLASK_APP'] = 'app.py'

handle_app_cors(app)
register_error_handlers(app)
