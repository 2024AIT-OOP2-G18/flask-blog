from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for
from model.comment import Comment

api_bp = Blueprint('api',__name__)


@api_bp.route('/comment',methods=['POST'])
def comment():
    try:
        # リクエストからブログIDとコメントを取得
        blog_id = request.form['blog_id']
        comment = request.form['comment']
        # コメントを保存
        Comment.create(blog_id=blog_id,comment=comment)
        return 200
    except:
        return 500

# いいね処理
@api_bp.route('/like/<int:blog_id>',methods=['POST'])
def like(blog_id):
    try:
        # IDが一致するブログを取得
        blog = Blog.get_by_id(blog_id)
        blog.likes += 1
        blog.save()
        return 200
    except Blog.DoesNotExist:
        return 404

# いいね解除処理
@api_bp.route('/unlike/<int:blog_id>',methods=['POST'])
def unlike(blog_id):
    try:
        # IDが一致するブログを取得
        blog = Blog.get_by_id(blog_id)
        blog.likes -= 1
        blog.save()
        return 200
    except Blog.DoesNotExist:
        return 404