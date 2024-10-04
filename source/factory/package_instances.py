from business_logic.utils.decorator_utils import singleton
from factory.flask_instance import db_instance, jwt_instance


def get_db_instance():
    return db_instance

@singleton
def get_jwt_instance():
    return jwt_instance

print("package_instances.py executed!")