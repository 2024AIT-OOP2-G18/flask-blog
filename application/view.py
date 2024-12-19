from model.blog import Blog

# ブログ一覧
def blog_list():
    blogs = Blog.select()
    # テストで要素を追加
    Blog.create(title="test", content="test")
    return "テスト追加しました"