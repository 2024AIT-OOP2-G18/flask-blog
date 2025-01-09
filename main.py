from flask import Flask, request, jsonify
from model import init_db
from application.create import create_bp
from application.view import *

app = Flask(__name__)
app.register_blueprint(create_bp)
app.register_blueprint(view_bp)

init_db()

# home
@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=8888)