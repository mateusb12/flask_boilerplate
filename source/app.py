import os

from business_logic.utils.env_utils import get_flask_debug_mode
from factory.flask_instance import app
from security.auth_endpoints import auth_bp

print("app.py executed!")
app.register_blueprint(auth_bp, url_prefix='/auth')


def __main__():
    port = int(os.environ.get("PORT", 5000))
    debug_mode = get_flask_debug_mode()
    # socket_instance.run(app, host='0.0.0.0', port=port, debug=debug_mode, allow_unsafe_werkzeug=True)
    app.run(host='0.0.0.0', port=port, debug=debug_mode)


if __name__ == "__main__":
    __main__()