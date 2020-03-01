from sqlalchemy.orm import sessionmaker

from ex_1_define_and_create_tables_orm import User, engine

ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")

ed_user.name
ed_user.nickname
str(ed_user.id)


Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name="ed").first()

ed_user is our_user

session.add_all(
    [
        User(name="wendy", fullname="Wendy Williams", nickname="windy"),
        User(name="mary", fullname="Mary Contrary", nickname="mary"),
        User(name="fred", fullname="Fred Flintstone", nickname="freddy"),
    ]
)

ed_user.nickname = "eddie"

session.dirty
session.new

session.commit()

# rolling back

ed_user.name = "Edwardo"
fake_user = User(name="fakeuser", fullname="Invalid", nickname="12345")
session.add(fake_user)
session.query(User).filter(User.name.in_(["Edwardo", "fakeuser"])).all()
session.rollback()

ed_user.name
fake_user in session
session.query(User).filter(User.name.in_(["ed", "fakeuser"])).all()
