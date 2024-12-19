from model.blog import Blog

# ブログ追加処理
def index():
    blogs = Blog.select()
    # テストで要素を追加
    Blog.create(title="test", content="test")
    return "テスト追加しました"