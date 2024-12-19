from model.blog import Blog

# ブログ一覧
def blog_list():
    blogs = Blog.select()
    for item in blogs:
        print("--------------")
        print(item.title)
        print(item.content)
        print("--------------")
    print(blogs)
    # テストで要素を追加
    return "テスト追加しました"

# ブログ詳細
def blog_detail(blog_id):
    try:
        blog = Blog.get_by_id(blog_id)
        return f"タイトル：{blog.title}<br>内容：{blog.content}<br>記載日時：{blog.created_at}"
    except Blog.DoesNotExist:
        return f"ID {blog_id} のブログは存在しません。"