from dotenv import load_dotenv
from sqlalchemy import create_engine

from factory.app_instance_creation import _create_postgres_connection_url

load_dotenv()
# Replace the placeholders with your actual database credentials
DATABASE_URI = _create_postgres_connection_url()

engine = create_engine(DATABASE_URI, echo=True)

# Try to connect to the database
try:
    connection = engine.connect()
    print("Connection is successful!")
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")
