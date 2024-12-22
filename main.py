from flask import Flask, request, jsonify
from model import init_db
from application.create import create_bp

app = Flask(__name__)
app.register_blueprint(create_bp)

init_db()

# home
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/view')
def viewe():
    return "any"


if __name__ == '__main__':

    app.run(debug=True)