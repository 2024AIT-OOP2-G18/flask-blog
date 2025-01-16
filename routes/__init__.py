from .create import create_bp
from .view import view_bp
from .api import api_bp
from .edit import edit_bp

blueprints = [
    create_bp,
    edit_bp,
    view_bp,
    api_bp,
]