from models.database_entities.user_model import SystemUser

print("populator.py imported!")

def populate_secondary_system_user():
    email = "test@example.com"
    username = "test_user"
    password = "123456"
    user_object = SystemUser(email, username)
    user_object.set_password(password)
    user_object.save()
    return user_object


def populate_pipeline():
    populate_secondary_system_user()
    print("Database populated!")


def main():
    populate_pipeline()


if __name__ == '__main__':
    main()
