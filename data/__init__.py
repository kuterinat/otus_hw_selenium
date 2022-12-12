import os.path


DATA_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(DATA_DIR, filename)


USER = get_path(filename="user.json")
PRODUCT = get_path(filename="product.json")
