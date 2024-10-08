from factory.app_instance_creation import create_flask_app
from models.data_transfer_objects.swagger_custom_api import CustomApi
from flask_socketio import SocketIO

app = create_flask_app(recreate_db=True)
swagger_api = CustomApi(app, version='1.0', title='Chat API', ordered=True)
socket_instance = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)

print("core_instances.py executed!")