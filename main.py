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

# 詳細表示
@app.route('/view/<int:blog_id>')
def view_detail(blog_id):
    return blog_detail(blog_id)

if __name__ == '__main__':
    
    app.run(debug=True)