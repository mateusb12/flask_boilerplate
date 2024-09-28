import os


def __main__():
    port = int(os.environ.get("PORT", 3000))
    debug_mode = get_flask_debug_mode()
    socket_instance.run(app, host='0.0.0.0', port=port, debug=debug_mode)


if __name__ == "__main__":
    __main__()