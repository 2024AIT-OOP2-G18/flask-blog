from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

# ブログ追加処理
create_bp = Blueprint('create',__name__, url_prefix="/create")

@create_bp.route('/',methods=['GET'])
def route():
    blogs = Blog.select()
    return render_template('create.html',blogs=blogs)

@create_bp.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        contents = request.form['contents']
        created_at = datetime.now()

        Blog.create(title=title, contents=contents,
                    likes=0, created_at =created_at)
        # db追加後のリダイレクト先
        return redirect(url_for('create.create_next',title=title,contents=contents))
    return render_template('create_next.html')  # GETリクエストの場合の処理

@create_bp.route('/next', methods=['GET'])
def create_next():
    title = request.args.get('title')
    contents = request.args.get('contents')

    return render_template('create_next.html',title=title,contents=contents)