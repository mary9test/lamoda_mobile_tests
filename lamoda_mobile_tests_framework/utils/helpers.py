import os


def abs_path(relative_path):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.join(root_path, relative_path)
