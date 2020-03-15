from wtforms import Form, StringField, TextAreaField, HiddenField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')


class TagForm(Form):
    name = StringField('name')


class CommentForm(Form):
    name = StringField('name')
    text = TextAreaField('text')
