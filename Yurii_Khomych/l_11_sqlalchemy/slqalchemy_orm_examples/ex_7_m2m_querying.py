from sqlalchemy.orm import sessionmaker, relationship

from ex_1_define_and_create_tables_orm import engine, User
from ex_6_many2many_relationships import BlogPost, Keyword

Session = sessionmaker(bind=engine)
session = Session()

wendy = session.query(User).filter_by(name="wendy").one()
post = BlogPost(
    headline="Wendy's Blog Post", body="This is a test", author=wendy
)
session.add(post)

post.keywords.append(Keyword("wendy"))
post.keywords.append(Keyword("firstpost"))

session.query(BlogPost).filter(
    BlogPost.keywords.any(keyword="firstpost")
).all()

session.query(BlogPost).filter(BlogPost.author == wendy).filter(
    BlogPost.keywords.any(keyword="firstpost")
).all()

wendy.posts.filter(BlogPost.keywords.any(keyword="firstpost")).all()
session.commit()
