from flask import Flask, request, jsonify, render_template
from model import init_db
from routes import blueprints

app = Flask(__name__)

init_db()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# home
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=8888)