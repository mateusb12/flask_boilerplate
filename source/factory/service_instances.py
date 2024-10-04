from service.system_user_service import SystemUserService

_system_user_service = None

def get_system_user_service():
    global _system_user_service
    if _system_user_service is None:
        _system_user_service = SystemUserService()
    return _system_user_service