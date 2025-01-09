from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for

view_bp = Blueprint('view',__name__)

# ブログ一覧
@view_bp.route('/view',methods=['GET'])
def view():
    blogs = Blog.select()
    return render_template('view.html',blogs=blogs)


# ブログ詳細
@view_bp.route('/view/<int:blog_id>',methods=['GET'])
def blog_detail(blog_id):
    try:
        # IDが一致するブログを取得
        blog = Blog.get_by_id(blog_id)
            
        print(blog)
        return "test"
        # return f"タイトル：{blog.title}<br>内容：{blog.content}<br>記載日時：{blog.created_at}"
    except Blog.DoesNotExist:
        return f"ID {blog_id} のブログは存在しません。"