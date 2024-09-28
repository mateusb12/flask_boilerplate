import os

from business_logic.utils.flask_utils import print_flask_logs


def print_env_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")


def str_to_bool(s):
    if s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    else:
        raise ValueError("Cannot convert {} to a bool".format(s))


def get_flask_debug_mode():
    variable = os.getenv("FLASK_DEBUG", "True")
    value = str_to_bool(variable)
    if not value:
        print_flask_logs()
    return value


def main():
    print_env_variables()


if __name__ == "__main__":
    main()
