from flask import Flask

from business_logic.utils.decorator_utils import singleton
from factory.flask_instance import _create_postgres_connection_url, handle_app_cors
from source.factory.package_instances import get_jwt_instance, get_db_instance
from source.paths.folder_reference import get_static_folder_path

from source.models.data_transfer_objects.flask_error_handlers import register_error_handlers
from dotenv import load_dotenv

db_instance = get_db_instance()
jwt_instance = get_jwt_instance()


@singleton
def create_flask_app(recreate_db: bool = False) -> Flask:
    load_dotenv()

    # Overall configs
    flask_app = Flask(__name__, static_folder=get_static_folder_path())
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = _create_postgres_connection_url()
    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['JWT_SECRET_KEY'] = 'marcelo'
    flask_app.config['FLASK_APP'] = 'app.py'

    jwt_instance.init_app(flask_app)
    db_instance.init_app(flask_app)
    register_error_handlers(flask_app)
    handle_app_cors(flask_app)

    # with flask_app.app_context():
    #     if recreate_db:
    #         _recreate_database_tables(db_instance)
    #     from database.populate.populator import populate_pipeline
    #     populate_pipeline()

    print("Flask app created! (app_instance_creation.py)")
    return flask_app


