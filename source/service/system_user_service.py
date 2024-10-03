from typing import List, Tuple


from business_logic.utils.jwt_utils import validate_token_and_get_message
from factory.app_instance_creation import create_flask_app
from factory.package_instances import db_instance
from models.data_transfer_objects.dto_custom_exceptions import EntityAlreadyExistsException, EntityNotFoundException, \
    MissingBodyParameterException, InvalidLoginCredentialsException
from models.database_entities.user_model import SystemUser
from repository.system_user_repository import SystemUserRepository


class SystemUserService:
    def __init__(self):
        self.system_user_repository = SystemUserRepository(db_instance)

    def register_user_service(self, data: dict) -> SystemUser:
        all_parameters = ["email", "username", "password"]
        email = data.get('email')
        if not email:
            raise MissingBodyParameterException("email", all_parameters)
        username = data.get('username')
        if not username:
            raise MissingBodyParameterException("username", all_parameters)
        password = data.get('password')
        if not password:
            raise MissingBodyParameterException("password", all_parameters)
        # if self.system_user_repository.get_user_by_email(email):
        #     raise EntityAlreadyExistsException(entity_tag="Email", entity=email)
        if self.system_user_repository.get_user_by_username(username):
            raise EntityAlreadyExistsException(entity_tag="Username", entity=username)
        user_object = SystemUser(email=email, username=username)
        user_object.set_password(password)
        return self.system_user_repository.create_user(user_object)

    def login_user_service(self, data: dict) -> SystemUser:
        all_parameters = ["login", "password"]
        login = data.get('login')
        if not login:
            raise MissingBodyParameterException("login", all_parameters)
        password = data.get('password')
        if not password:
            raise MissingBodyParameterException("password", all_parameters)
        user = self.system_user_repository.get_user_by_email(login)
        if not user:
            raise InvalidLoginCredentialsException()
        if not user.check_password(password):
            raise InvalidLoginCredentialsException()
        return user

    def find_user_by_id(self, user_id) -> SystemUser:
        query_result = self.system_user_repository.get_user_by_id(user_id)
        if not isinstance(query_result, SystemUser):
            raise EntityNotFoundException("User", user_id)
        return query_result

    def find_user_by_email(self, email) -> SystemUser:
        query_result = self.system_user_repository.get_user_by_email(email)
        if not isinstance(query_result, SystemUser):
            raise EntityNotFoundException("User", email)
        return query_result

    def find_all_users(self) -> Tuple[List[SystemUser], str]:
        token_message = validate_token_and_get_message()
        return self.system_user_repository.get_all_users(), token_message

    def modify_user(self, user_id, **kwargs) -> SystemUser or None:  # type: ignore
        user: SystemUser = self.system_user_repository.get_user_by_id(user_id)
        if not isinstance(user, SystemUser):
            raise EntityNotFoundException("User", user_id)
        return self.system_user_repository.update_user(user_id, **kwargs)

    def remove_user(self, user_id) -> bool:
        # Business logic before user deletion, like checking user activity or dependencies
        user: SystemUser = self.system_user_repository.get_user_by_id(user_id)
        if not isinstance(user, SystemUser):
            raise EntityNotFoundException("User", user_id)
        return self.system_user_repository.delete_user(user_id)


# Example usage
def __main():
    app = create_flask_app()
    with app.app_context():
        user_service = SystemUserService()
        user = user_service.find_user_by_id(13)
        print(user)


if __name__ == "__main__":
    __main()