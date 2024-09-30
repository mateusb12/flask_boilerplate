import os

from business_logic.utils.env_utils import get_flask_debug_mode
from factory.core_instances import socket_instance, app


def __main__():
    print("app.py execution!")
    port = int(os.environ.get("PORT", 3000))
    debug_mode = get_flask_debug_mode()
    # socket_instance.run(app, host='0.0.0.0', port=port, debug=debug_mode, allow_unsafe_werkzeug=True)
    app.run(host='0.0.0.0', port=port, debug=debug_mode)


if __name__ == "__main__":
    __main__()