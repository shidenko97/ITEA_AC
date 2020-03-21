from datetime import datetime
from blog import db
from blog.posts.utils import slugify


post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id',
                                                   ondelete="CASCADE")),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id', ondelete="CASCADE"))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    like_count = db.Column(db.Integer, default=0, nullable=False)
    dislike_count = db.Column(db.Integer, default=0, nullable=False)
    tags = db.relationship(
        'Tag',
        secondary=post_tags,
        backref=db.backref('posts', lazy='dynamic'),
        cascade="all,delete"
    )
    comments = db.relationship('Comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return f'<Tag id: {self.id}, name: {self.name}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column('post_id',
                        db.Integer,
                        db.ForeignKey('post.id', ondelete="CASCADE"))
    name = db.Column(db.Text)
    text = db.Column(db.Text)
    datetime = db.Column(db.DateTime, default=datetime.now())
