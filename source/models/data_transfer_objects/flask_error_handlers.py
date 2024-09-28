from datetime import datetime

from flask import make_response, jsonify

from models.data_transfer_objects.custom_exception_pool import EXCEPTIONS
from models.data_transfer_objects.dto_core_model import response_error_dto


def handle_generic_exception(error):
    response = response_error_dto(
        status_code=error.status_code,
        error_type=error.error_type,
        message=error.message,
        description=error.description
    )
    return make_response(jsonify(response), error.status_code)


def register_error_handlers(app):
    for item in EXCEPTIONS:
        app.register_error_handler(item, handle_generic_exception)

    @app.errorhandler(404)
    def handle_404_error(error):
        response = response_error_dto(
            status_code=404,
            error_type="NotFoundError",
            message="Resource not found!",
            description="The requested resource could not be found."
        )
        return make_response(jsonify(response), 404)