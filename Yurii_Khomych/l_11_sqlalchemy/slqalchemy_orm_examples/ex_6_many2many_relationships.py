from sqlalchemy import Table, Text, ForeignKey, Column, Integer, String

# association table
from sqlalchemy.orm import relationship

from ex_1_define_and_create_tables_orm import Base, create_tables, engine, User

post_keywords = Table(
    "post_keywords",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("keyword_id", ForeignKey("keywords.id"), primary_key=True),
)
# (1, 1)
# (1, 2)


class BlogPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    # many to many BlogPost<->Keyword
    keywords = relationship(
        "Keyword", secondary=post_keywords, back_populates="posts"
    )

    author = relationship("User", back_populates="posts")

    def __init__(self, headline, body, author):
        self.headline = headline
        self.body = body
        self.author = author

    def __repr__(self):
        return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)


class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship(
        "BlogPost", secondary=post_keywords, back_populates="keywords"
    )

    def __init__(self, keyword):
        self.keyword = keyword


BlogPost.author = relationship(User, back_populates="posts")
User.posts = relationship(BlogPost, back_populates="author", lazy="dynamic")

if __name__ == "__main__":
    create_tables(Base, engine=engine)
