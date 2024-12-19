from peewee import *
import datetime

from peewee import Model, CharField, SqliteDatabase

# ブログモデル
db = SqliteDatabase('database.db')
class Blog(Model):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db