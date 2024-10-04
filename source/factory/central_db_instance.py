from flask_sqlalchemy import SQLAlchemy
from factory.flask_instance import app

db_instance = SQLAlchemy(app)