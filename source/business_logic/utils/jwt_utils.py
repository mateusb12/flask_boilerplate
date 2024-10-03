from datetime import datetime as dt, timedelta, datetime

import jwt
from flask_jwt_extended import get_jwt

from models.data_transfer_objects.dto_custom_exceptions import TokenNotAvailableException
from security.jwt_error_handlers import timedelta_to_str


def get_token_remaining_life_seconds(claims: dict) -> timedelta:
    expiry_timestamp = claims['exp']
    current_time = dt.utcnow()
    expiry_time = dt.utcfromtimestamp(expiry_timestamp)
    remaining_life = expiry_time - current_time
    return remaining_life


def validate_token_and_get_message():
    claims = get_jwt()
    remaining_life = get_token_remaining_life_seconds(claims)
    jti = claims['jti']
    # token_object = TokenBlockList(jti=jti)
    # if token_object.is_token_expired():
    #     raise TokenNotAvailableException()
    token_timestamp = timedelta_to_str(remaining_life)
    return f'Token expires in {token_timestamp}'


def is_token_expired(decoded_token):
    return datetime.utcnow() > datetime.utcfromtimestamp(decoded_token['exp'])


def check_for_token_expiration(SECRET_KEY: str, token: str):
    jwt.decode(token[7:], SECRET_KEY, algorithms=["HS256"])


def decode_jwt_token(SECRET_KEY, token):
    return jwt.decode(token[7:], SECRET_KEY, algorithms=["HS256"], options={"verify_exp": False})