from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.exc import IntegrityError
from factory.package_instances import db_instance as db


class TokenBlockList(db.Model):
    __tablename__ = 'token_block_list'
    id = Column(Integer, primary_key=True)
    jti = Column(String(36), nullable=False)
    created_at = Column(Float, default=db.func.current_timestamp(), nullable=False)

    def __init__(self, jti, created_at=None):
        self.jti = jti
        if created_at is not None:
            self.created_at = created_at

    def __repr__(self):
        return f"<TokenBlockList jti={self.jti}, created_at={self.created_at}>"

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise e

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def is_token_expired(self):
        token_timestamp = self.created_at
        current_timestamp = db.func.current_timestamp()
        return token_timestamp < current_timestamp


    # @classmethod
    # def list_all_expired_tokens(cls):
    #     current_timestamp = db.func.current_timestamp()
    #     return cls.query.filter(cls.created_at < current_timestamp).all()
    #
    # @classmethod
    # def delete_all_expired_tokens(cls):
    #     current_timestamp = db.func.current_timestamp()
    #     expired_tokens = cls.query.filter(cls.created_at < current_timestamp).all()
    #     for token in expired_tokens:
    #         db.session.delete(token)
    #     db.session.commit()