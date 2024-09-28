from sqlalchemy.exc import IntegrityError
from datetime import datetime
from factory.package_instances import db_instance as db


class ResetPasswordToken(db.Model):
    __tablename__ = 'ResetPasswordToken'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token: str = db.Column(db.String(255), nullable=False)
    expiration_time: datetime = db.Column(db.DateTime, nullable=False)

    system_user_id: int = db.Column(db.Integer, db.ForeignKey('SystemUser.id'), nullable=False)

    def __init__(self, token: str, expiration_time: datetime, system_user_id: int):
        self.token = token
        self.expiration_time = expiration_time
        self.system_user_id = system_user_id

    def __repr__(self):
        return f"<ResetPasswordToken [{self.id}] from [{self.system_user_id}]>"

    def __iter__(self):
        yield 'id', self.id
        yield 'token', self.token
        yield 'expiration_time', self.expiration_time.isoformat() if self.expiration_time else None
        yield 'system_user_id', self.system_user_id

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise

    def delete(self):
        db.session.delete(self)
        db.session.commit()