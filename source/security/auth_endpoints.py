from time import time
from datetime import timedelta
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt
from werkzeug.exceptions import UnsupportedMediaType
from flask_jwt_extended import create_refresh_token, jwt_required

from source.models.database_entities.token_block_list_model import TokenBlockList
from source.factory.package_instances import jwt_instance
from source.factory.service_instances import get_system_user_service
from security.jwt_error_handlers import timedelta_to_str

auth_bp = Blueprint('auth', __name__)
EXPIRE_TIME_SECONDS = timedelta(hours=20)
REFRESH_TOKEN_DURATION = timedelta(seconds=100)


@auth_bp.post('/login')
def login_user():
    try:
        data = request.get_json()
    except UnsupportedMediaType as e:
        return jsonify({'error': 'Invalid or missing JSON body', 'details': str(e)}), 400
    user = get_system_user_service().login_user_service(data)
    login = data.get('login')
    access_token = create_access_token(identity=login, expires_delta=EXPIRE_TIME_SECONDS)
    refresh_token = create_refresh_token(identity=login, expires_delta=EXPIRE_TIME_SECONDS)
    tokens = {"access_token": access_token,
              "refresh_token": refresh_token}
    return jsonify({'username': user.username, 'tokens': tokens}), 200


@auth_bp.post('/register')
def register_user():
    try:
        data = request.get_json()
    except UnsupportedMediaType as e:
        return jsonify({'error': 'Invalid or missing JSON body', 'details': str(e)}), 400
    result = system_user_service.register_user_service(data)
    return jsonify({'message': 'User created!', 'data': dict(result)}), 201


@auth_bp.post('/refresh_token')
def refresh():
    current_user = get_jwt()
    new_token = create_access_token(identity=current_user, expires_delta=REFRESH_TOKEN_DURATION)
    new_duration = timedelta_to_str(REFRESH_TOKEN_DURATION)
    return (
        jsonify({'message': f'Token refreshed! New duration: {new_duration}s',
                 'new_token': new_token}),
        200)


@auth_bp.get('/get_user_claims')
def who_am_i():
    claims = get_jwt()
    return jsonify({'claims': claims}), 200


@auth_bp.delete('/logout')
def logout_user():
    jti = get_jwt()['jti']
    token = TokenBlockList(jti=jti, created_at=time())
    token.save()
    return jsonify({'message': 'User logged out!'}), 200


@jwt_instance.additional_claims_loader
def claim_automatic_creator(identity):
    additional_claims = {}
    if identity == "zezim123":
        additional_claims["is_staff"] = True
    return additional_claims