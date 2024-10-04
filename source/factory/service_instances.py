from business_logic.utils.decorator_utils import singleton
from service.system_user_service import SystemUserService

@singleton
def get_system_user_service():
    print("service_instances.py executed!")
    return SystemUserService()