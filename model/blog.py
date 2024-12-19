from peewee import *
import datetime

class Blog(Model):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)