from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

# ブログ追加処理
edit_bp = Blueprint('edit',__name__, url_prefix="/edit")

@edit_bp.route('/<int:blog_id>',methods=['GET','POST'])
def route(blog_id):
    if request.method == 'GET':
        blog = Blog.get_by_id(blog_id)
        return render_template('edit.html',blog=blog)
    if request.method == 'POST':
        print("POST")
        title = request.form['title']
        contents = request.form['contents']
        blog = Blog.get_by_id(blog_id)
        blog.title = title
        blog.contents = contents
        blog.updated_at = datetime.now()
        blog.save()
        return redirect(url_for('view.blog_detail',blog_id=blog_id))