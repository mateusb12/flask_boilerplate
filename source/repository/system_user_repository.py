from typing import List

from factory.app_instance_creation import create_flask_app
from typing import Optional

from factory.package_instances import get_db_instance
from models.database_entities.user_model import SystemUser

db_instance = get_db_instance()


class SystemUserRepository:
    def __init__(self, input_db_instance):
        self.db = input_db_instance

    def create_user(self, user_object: SystemUser) -> SystemUser:
        user_object.save()
        return user_object

    def get_user_by_id(self, user_id: int) -> SystemUser:
        return self.db.session.get(SystemUser, user_id)

    def get_user_by_email(self, email: str) -> SystemUser:
        return self.db.session.query(SystemUser).filter_by(email=email).first()

    def get_user_by_username(self, username: str) -> SystemUser:
        return self.db.session.query(SystemUser).filter_by(username=username).first()

    def get_all_users(self) -> List[SystemUser]:
        return self.db.session.query(SystemUser).all()

    def update_user(self, user_id: int, **kwargs) -> Optional[SystemUser]:
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.db.session.commit()
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.db.session.delete(user)
            self.db.session.commit()
            return True
        return False


def __main():
    app = create_flask_app()
    with app.app_context():
        user_repository = SystemUserRepository(db_instance)
        all_users = user_repository.get_all_users()
        print(all_users)


if __name__ == "__main__":
    __main()