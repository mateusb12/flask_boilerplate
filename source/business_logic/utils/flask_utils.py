from datetime import datetime
from flask import request

STATUS_COLOR_CODES = {
    'success': "\033[92m",  # Green
    'redirect': "\033[93m",  # Yellow
    'client_error': "\033[91m",  # Red
    'server_error': "\033[91m",  # Red
    'other': "\033[96m"  # Cyan
}

METHOD_COLOR_CODES = {
    'GET': "\033[95m",  # Blue
    'POST': "\033[92m",  # Green
    'PUT': "\033[33m",  # Orange
    'DELETE': "\033[91m",  # Red
    'PATCH': "\033[95m",  # Purple "\033[94m"
    'HEAD': "\033[96m",  # Cyan
    'OPTIONS': "\033[97m"  # White
}

STATUS_CODE_RANGES = {
    range(200, 300): STATUS_COLOR_CODES['success'],
    range(300, 400): STATUS_COLOR_CODES['redirect'],
    range(400, 500): STATUS_COLOR_CODES['client_error'],
    range(500, 600): STATUS_COLOR_CODES['server_error'],
}

DEFAULT_COLOR = "\033[91m"
RESET_COLOR = "\033[0m"


def get_method_color(http_method):
    return METHOD_COLOR_CODES.get(http_method, "\033[97m")


def get_status_color(response_status_code):
    for status_range, color in STATUS_CODE_RANGES.items():
        if response_status_code in status_range:
            return color
    return STATUS_COLOR_CODES['other']


def log_http_request(response):
    now = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
    server_protocol = request.environ.get("SERVER_PROTOCOL", "")

    status_color = get_status_color(response.status_code)
    method_color = get_method_color(request.method)

    # The log entry starts with the default red color and uses specific colors for method and status
    log_entry = (
        f'{DEFAULT_COLOR}{request.remote_addr} - - [{now}] {method_color}{request.method}{RESET_COLOR} "{request.path}"'
        f' {status_color}{response.status_code}{DEFAULT_COLOR} -{RESET_COLOR}')

    print(log_entry)


def print_flask_logs():
    # print('* Serving Flask app')
    print('\033[91m* Running on http://localhost:3000/\033[0m')
    # print('\033[33m* Press Ctrl+C to quit\033[0m')