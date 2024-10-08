from datetime import datetime

def response_error_dto(status_code: int, error_type: str, message: str, description: str):
    return {
        "ResponseErrorDTO": {
            "statusCode": status_code,
            "type": error_type,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "message": message,
            "description": description
        }
    }