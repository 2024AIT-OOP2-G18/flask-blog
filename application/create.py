from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

# ブログ追加処理
create_bp = Blueprint('create',__name__)

@create_bp.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        contents = request.form['contents']
        likes = int(request.form['likes'])
        created_at = datetime.now()

        Blog.create(title=title, contents=contents,
                    likes=likes, created_at =created_at)

        # db追加後のリダイレクト先
        return redirect(url_for('any'))

    return render_template('any')
