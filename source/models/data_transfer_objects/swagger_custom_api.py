import werkzeug
from flask import make_response, jsonify
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restx import Api
from jwt import InvalidTokenError, ExpiredSignatureError

from models.data_transfer_objects.custom_exception_pool import EXCEPTIONS
from models.data_transfer_objects.dto_core_model import response_error_dto
from security import jwt_error_handlers


class CustomApi(Api):
    def __init__(self, *args, **kwargs):
        super(CustomApi, self).__init__(*args, **kwargs)
        self._register_jwt_error_handlers()

    def handle_error(self, e):
        # Check for custom exceptions first
        if isinstance(e, tuple(EXCEPTIONS)):
            return self._handle_custom_exception(e)
        # Handle 404 and other Werkzeug exceptions
        elif isinstance(e, werkzeug.exceptions.HTTPException):
            return self._handle_http_exception(e)
        # Fallback to the original handler for all other errors
        return super(CustomApi, self).handle_error(e)

    def _register_jwt_error_handlers(self):
        @self.errorhandler(ExpiredSignatureError)
        def handle_expired_error(e):
            return jwt_error_handlers.expired_token_callback(e.jwt_header, e.jwt_data)

        @self.errorhandler(InvalidTokenError)
        def handle_invalid_token_error(e):
            return jwt_error_handlers.invalid_token_callback(str(e))

        @self.errorhandler(NoAuthorizationError)
        def handle_missing_token_error(e):
            return jwt_error_handlers.missing_token_callback(str(e))

    def _handle_custom_exception(self, e):
        # Handle custom exceptions here
        response = response_error_dto(
            status_code=e.status_code,
            error_type=e.__class__.__name__,
            message=e.message,
            description=e.description
        )
        return make_response(jsonify(response), e.status_code)

    def _handle_http_exception(self, e):
        # Example: Handle 404 Not Found specifically
        if isinstance(e, werkzeug.exceptions.NotFound):
            response = response_error_dto(
                status_code=404,
                error_type="NotFoundError",
                message="The requested resource was not found",
                description="Custom 404 error description"
            )
            return make_response(jsonify(response), 404)
        # Handle other HTTP exceptions as needed
        return super(CustomApi, self).handle_error(e)