from datetime import datetime

from factory.package_instances import jwt_instance


@jwt_instance.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    expiration_time = datetime.utcfromtimestamp(jwt_data['exp'])
    now = datetime.utcnow()
    time_diff = (now - expiration_time)
    time_diff_string = timedelta_to_str(time_diff)
    return {
        'message': f'The token has expired {time_diff_string} ago',
        'error': 'token_expired'
    }, 401


@jwt_instance.invalid_token_loader
def invalid_token_callback(error):
    return {
        'message': f'The provided token is invalid. [{error}]',
        'error': 'invalid_token'
    }, 401


@jwt_instance.unauthorized_loader
def missing_token_callback(error):
    return {
        'message': 'Request does not contain an access token',
        'error': 'authorization_required'
    }, 401


# @jwt_instance.token_in_blocklist_loader
# def check_if_token_in_blacklist_callback(jwt_header, jwt_data):
#     jti = jwt_data['jti']
#     token = db_instance.session.query(TokenBlockList.id).filter_by(jti=jti).scalar()
#     return token is not None

def timedelta_to_str(delta):
    """
    Converts a timedelta to a human-readable string.

    Args:
    - delta (timedelta): The timedelta object to be converted.

    Returns:
    - str: A string in the format "X h Y min Z s".
    """
    total_seconds = int(delta.total_seconds())  # Getting the total seconds from the timedelta
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Formatting the string
    formatted_str = ""
    if hours:
        formatted_str += f"{hours}h "
    if minutes:
        formatted_str += f"{minutes}min "
    if seconds or not formatted_str:  # Ensure we return "0s" if delta is very small
        formatted_str += f"{seconds}s"

    return formatted_str.strip()