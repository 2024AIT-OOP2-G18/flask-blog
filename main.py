from flask import Flask, request, jsonify
from application.__init__ import *
from application.view import *
from application.create import *

app = Flask(__name__)


init_db()


# home
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/view')
def viewe():
    return blog_list()


if __name__ == '__main__':
    
    app.run(debug=True)