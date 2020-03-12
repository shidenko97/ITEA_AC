from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, aliased

from ex_1_define_and_create_tables_orm import User, engine
from ex_4_relationships import Address

Session = sessionmaker(bind=engine)
session = Session()

jack = User(name="jack", fullname="Jack Bean", nickname="gjffdd")
jack.addresses

jack.addresses = [
    Address(email_address="jack@google.com"),
    Address(email_address="j25@yahoo.com"),
]
session.add(jack)
session.commit()

# jack = session.query(User).filter_by(name="jack").one()
jack.addresses

# Querying with join
for u, a in (
    session.query(User, Address)
    .filter(User.id == Address.user_id)
    .filter(Address.email_address == "jack@google.com")
    .all()
):
    print(u)
    print(a)

session.query(User).join(Address).filter(
    Address.email_address == "jack@google.com"
).all()

# query.join(Address, User.id==Address.user_id)    # explicit condition
# query.join(User.addresses)                       # specify relationship from left to right
# query.join(Address, User.addresses)              # same, with explicit target
# query.join('addresses')                          # same, using a string
# query.outerjoin(User.addresses)

adalias1 = aliased(Address)
adalias2 = aliased(Address)
for username, email1, email2 in (
    session.query(User.name, adalias1.email_address, adalias2.email_address)
    .join(adalias1, User.addresses)
    .join(adalias2, User.addresses)
    .filter(adalias1.email_address == "jack@google.com")
    .filter(adalias2.email_address == "j25@yahoo.com")
):
    print(username, email1, email2)

# With subquery
stmt = (
    session.query(Address.user_id, func.count("*").label("address_count"))
    .group_by(Address.user_id)
    .subquery()
)

for u, count in (
    session.query(User, stmt.c.address_count)
    .outerjoin(stmt, User.id == stmt.c.user_id)
    .order_by(User.id)
):
    print(u, count)

# Deleting
session.delete(jack)

session.query(User).filter_by(name="jack").count()
# But
session.query(Address).filter(
    Address.email_address.in_(["jack@google.com", "j25@yahoo.com"])
).count()

session.close()
# ROLLBACK
# Add to Users cascade delete

jack = session.query(User).get(5)
del jack.addresses[1]
session.query(Address).filter(
    Address.email_address.in_(["jack@google.com", "j25@yahoo.com"])
).count()

session.delete(jack)
session.query(User).filter_by(name="jack").count()
session.query(Address).filter(
    Address.email_address.in_(["jack@google.com", "j25@yahoo.com"])
).count()
