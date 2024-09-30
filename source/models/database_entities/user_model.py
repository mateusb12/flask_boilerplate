import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from business_logic.utils.exception_utils import handle_integrity_error
from source.factory.package_instances import db_instance as db

print("user_model.py imported!")


class SystemUser(db.Model):
    __tablename__ = 'SystemUser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # chats = db.relationship('Chat', backref='user', foreign_keys=[Chat.user_id])

    def __init__(self, email: str, username: str):
        self.email = email
        self.username = username

    def __repr__(self):
        return f"<User [{self.email}], [{self.username}]>"

    def __iter__(self):
        yield 'id', self.id
        yield 'email', self.email
        yield 'username', self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            handle_integrity_error(e, self.__tablename__, ['email', 'username'], self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()