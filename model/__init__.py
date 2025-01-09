from model.blog import Blog
from peewee import Model, CharField, SqliteDatabase

db = SqliteDatabase('database.db')
# DB初期化
def init_db():
    print("init_db")
    db.connect()
    db.create_tables([Blog], safe=True)
    db.close()

# DB接続
def connect_db():
    print("connect_db")
    db.connect()