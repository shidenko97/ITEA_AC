import datetime

from mongoengine import Document, StringField, ReferenceField, DateTimeField


class Author(Document):
    name = StringField()


class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
    # author = ReferenceField(Author)
