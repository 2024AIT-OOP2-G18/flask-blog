from peewee import Model, SqliteDatabase, CharField, TextField, IntegerField, DateTimeField

# ブログモデル
db = SqliteDatabase('database.db')
class Blog(Model):
    title = CharField()
    contents = TextField()
    likes = IntegerField()
    created_at = DateTimeField()
    class Meta:
        database = db