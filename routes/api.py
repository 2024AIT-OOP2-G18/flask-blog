from model.blog import Blog
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from model.comment import Comment
from datetime import datetime


api_bp = Blueprint('api',__name__)

@api_bp.route('/comment',methods=['POST'])
def comment():
    try:
        # リクエストからブログIDとコメントを取得
        blog_id = request.form['blog_id']
        comment = request.form['comment']
        created_at = datetime.now()
        print(blog_id,comment)
        
        Comment.create(blog_id=blog_id,comment=comment,created_at=created_at)
        
        return jsonify(status="success", code=200)
    except:
        print("error")
        return jsonify(status="fail", code=404)

# いいね処理
@api_bp.route('/like', methods=['POST'])
def like():
    try:
        blog_id = request.form['blog_id']
        # IDが一致するブログを取得
        blog = Blog.get_by_id(blog_id)
        blog.likes += 1
        blog.save()
        return jsonify(status="success", code=200)
    except Blog.DoesNotExist:
        return jsonify(status="fail", code=404)