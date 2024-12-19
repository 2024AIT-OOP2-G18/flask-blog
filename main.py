from flask import Flask, request, jsonify



app = Flask(__name__)

# home
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)