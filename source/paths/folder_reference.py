import os
from pathlib import Path


def get_source_folder_path() -> Path:
    return Path(os.path.dirname(os.path.realpath(__file__))).parent


def get_root_folder_path() -> Path:
    return Path(os.path.dirname(os.path.realpath(__file__))).parent.parent


def get_static_folder_path() -> Path:
    return get_root_folder_path() / "static"
