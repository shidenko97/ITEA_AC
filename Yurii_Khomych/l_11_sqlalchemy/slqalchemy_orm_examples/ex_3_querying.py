from sqlalchemy.orm import sessionmaker, aliased

from ex_1_define_and_create_tables_orm import User, engine

Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label("name_label")).all():
    print(row.name_label)

user_alias = aliased(User, name="user_alias")
for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

for (name,) in session.query(User.name).filter_by(fullname="Ed Jones"):
    print(name)

for (name,) in session.query(User.name).filter(User.fullname == "Ed Jones"):
    print(name)

for user in (
    session.query(User)
    .filter(User.name == "ed")
    .filter(User.fullname == "Ed Jones")
):
    print(user)

# equals:
# query.filter(User.name == 'ed')
# not equals:
# query.filter(User.name != 'ed')
# LIKE:
# query.filter(User.name.like('%ed%'))
# ILIKE (case-insensitive LIKE):
# query.filter(User.name.ilike('%ed%'))

# IN:
# query.filter(User.name.in_(['ed', 'wendy', 'jack']))
#
# works with query objects too:
# query.filter(User.name.in_(
#     session.query(User.name).filter(User.name.like('%ed%'))
# ))
#
# use tuple_() for composite (multi-column) queries
# from sqlalchemy import tuple_
# query.filter(
#     tuple_(User.name, User.nickname).\
#     in_([('ed', 'edsnickname'), ('wendy', 'windy')])
# )

# NOT IN:
# query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
# IS NULL:
# query.filter(User.name == None)

# alternatively, if pep8/linters are a concern
# query.filter(User.name.is_(None))
# IS NOT NULL:
# query.filter(User.name != None)

# alternatively, if pep8/linters are a concern
# query.filter(User.name.isnot(None))
# AND:
# use and_()
# from sqlalchemy import and_
# query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
# query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
# query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
# OR:
# from sqlalchemy import or_
# query.filter(or_(User.name == 'ed', User.name == 'wendy'))
# MATCH:
# query.filter(User.name.match('wendy'))

# all() returns a list:
query = session.query(User).filter(User.name.like("%ed")).order_by(User.id)
query.all()

# first() applies a limit of one and returns the first result as a scalar:
query.first()
# one() fully fetches all rows, and if not exactly one object identity or composite row is present in the result, raises an error. With multiple rows found:
user = query.one()
user = query.filter(User.id == 99).one()
# one_or_none() is like one()
user = query.filter(User.id == 99).one_or_none()
query = session.query(User.id).filter(User.name == "ed").order_by(User.id)
query.scalar()

session.query(User).filter(User.name.like("%ed")).count()
