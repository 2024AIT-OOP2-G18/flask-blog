from .create import create_bp
from .view import view_bp
from .api import api_bp

blueprints = [
    create_bp,
    view_bp,
    api_bp,
]