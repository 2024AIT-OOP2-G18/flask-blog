from model.blog import Blog
from model.comment import Comment
from peewee import Model, CharField, SqliteDatabase

db = SqliteDatabase('database.db')
# DB初期化
def init_db():
    print("init_db")
    db.connect()
    db.create_tables([Blog, Comment], safe=True)
    db.close()

# DB接続
def connect_db():
    print("connect_db")
    db.connect()