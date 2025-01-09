from peewee import Model, SqliteDatabase, CharField, TextField, IntegerField, DateTimeField, ForeignKeyField
from model.blog import Blog

# commentモデル
db = SqliteDatabase('database.db')
class Comment(Model):
    blog = ForeignKeyField(Blog, backref='comments')  # 外部キーを追加
    comment = TextField()
    created_at = DateTimeField()
    class Meta:
        database = db