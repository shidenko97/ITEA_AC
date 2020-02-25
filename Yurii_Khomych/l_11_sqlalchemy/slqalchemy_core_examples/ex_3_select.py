from sqlalchemy import select, or_, text, func, desc, bindparam, and_, not_

from ex_1_define_and_create_tables_core import (
    users,
    addresses,
    engine,
)

conn = engine.connect()

s = select([users])
result = conn.execute(s)
# SELECT users.id, users.name, users.fullname
# FROM users
# ()
for row in result:
    print(row)

result = conn.execute(s)
row = result.fetchone()
print("name:", row["name"], "; fullname:", row["fullname"])


result = conn.execute(s)
row = result.fetchone()
print("name:", row[1], "; fullname:", row[2])

for row in conn.execute(s):
    print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])

result.close()

s = select([users.c.name, users.c.fullname])
result = conn.execute(s)
for row in result:
    print(row)

# But
for row in conn.execute(select([users, addresses])):
    print(row)

s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
for row in conn.execute(s):
    print(row)

# todo continue from this line
# operators
print(users.c.id == addresses.c.user_id)
print(users.c.id == 7)
(users.c.id == 7).compile().params
print(users.c.id != 7)
print(users.c.name == None)
print("fred" > users.c.name)
print(users.c.id + addresses.c.id)
print(users.c.name + users.c.fullname)


print(
    and_(
        users.c.name.like("j%"),
        users.c.id == addresses.c.user_id,
        or_(
            addresses.c.email_address == "wendy@aol.com",
            addresses.c.email_address == "jack@yahoo.com",
        ),
        not_(users.c.id > 5),
    )
)

print(
    users.c.name.like("j%")
    & (users.c.id == addresses.c.user_id)
    & (
        (addresses.c.email_address == "wendy@aol.com")
        | (addresses.c.email_address == "jack@yahoo.com")
    )
    & ~(users.c.id > 5)
)

s = select(
    [(users.c.fullname + ", " + addresses.c.email_address).label("title")]
).where(
    and_(
        users.c.id == addresses.c.user_id,
        users.c.name.between("e", "z"),
        or_(
            addresses.c.email_address.like("%@aol.com"),
            addresses.c.email_address.like("%@msn.com"),
        ),
    )
)
res = conn.execute(s).fetchall()

s = (
    select(
        [(users.c.fullname + ", " + addresses.c.email_address).label("title")]
    )
    .where(users.c.id == addresses.c.user_id)
    .where(users.c.name.between("m", "z"))
    .where(
        or_(
            addresses.c.email_address.like("%@aol.com"),
            addresses.c.email_address.like("%@msn.com"),
        )
    )
)
conn.execute(s).fetchall()

res = conn.execute(s).fetchall()

s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
    "FROM users, addresses "
    "WHERE users.id = addresses.user_id "
    "AND users.name BETWEEN :x AND :y "
    "AND (addresses.email_address LIKE :e1 "
    "OR addresses.email_address LIKE :e2)"
)
conn.execute(s, x="m", y="z", e1="%@aol.com", e2="%@msn.com").fetchall()


stmt = (
    select(
        [
            addresses.c.user_id,
            func.count(addresses.c.id).label("num_addresses"),
        ]
    )
    .group_by("user_id")
    .order_by("user_id", "num_addresses")
)
res = conn.execute(stmt).fetchall()
stmt = (
    select(
        [
            addresses.c.user_id,
            func.count(addresses.c.id).label("num_addresses"),
        ]
    )
    .group_by("user_id")
    .order_by("user_id", desc("num_addresses"))
)

res = conn.execute(stmt).fetchall()

u1a, u1b = users.alias(), users.alias()
stmt = (
    select([u1a, u1b]).where(u1a.c.name > u1b.c.name).order_by(u1a.c.name)
)  # using "name" here would be ambiguous

conn.execute(stmt).fetchall()


a1 = addresses.alias()
a2 = addresses.alias()
s = select([users]).where(
    and_(
        users.c.id == a1.c.user_id,
        users.c.id == a2.c.user_id,
        a1.c.email_address == "jack@msn.com",
        a2.c.email_address == "jack@yahoo.com",
    )
)
res = conn.execute(s).fetchall()

# Joins
print(users.join(addresses))
print(
    users.join(addresses, addresses.c.email_address.like(users.c.name + "%"))
)

s = select([users.c.fullname]).select_from(
    users.join(addresses, addresses.c.email_address.like(users.c.name + "%"))
)

res = conn.execute(s).fetchall()

s = select([users.c.fullname]).select_from(users.outerjoin(addresses))
print(s)

# Subqueries
stmt = (
    select([addresses.c.user_id])
    .where(addresses.c.user_id == users.c.id)
    .where(addresses.c.email_address == "jack@yahoo.com")
)
enclosing_stmt = select([users.c.name]).where(users.c.id == stmt)
# SELECT users.name
# FROM users
# WHERE users.id = (SELECT addresses.user_id
#     FROM addresses
#     WHERE addresses.user_id = users.id
#     AND addresses.email_address = ?)
# ('jack@yahoo.com',)
res = conn.execute(enclosing_stmt).fetchall()

stmt = select([users.c.name]).order_by(users.c.name)
res = conn.execute(stmt).fetchall()

stmt = select([users.c.name]).order_by(users.c.name.desc())
res = conn.execute(stmt).fetchall()

tmt = (
    select([users.c.name, func.count(addresses.c.id)])
    .select_from(users.join(addresses))
    .group_by(users.c.name)
)
conn.execute(stmt).fetchall()

stmt = (
    select([users.c.name, func.count(addresses.c.id)])
    .select_from(users.join(addresses))
    .group_by(users.c.name)
    .having(func.length(users.c.name) > 4)
)
res = conn.execute(stmt).fetchall()

# Distinct
stmt = (
    select([users.c.name])
    .where(addresses.c.email_address.contains(users.c.name))
    .distinct()
)
conn.execute(stmt).fetchall()

# Insert update delete
stmt = users.update().values(fullname="Fullname: " + users.c.name)
# UPDATE users SET fullname=(? || users.name)
# ('Fullname: ',)
# COMMIT
conn.execute(stmt)

stmt = users.insert().values(name=bindparam("_name") + " .. name")
conn.execute(
    stmt,
    [
        {"id": 4, "_name": "name1"},
        {"id": 5, "_name": "name2"},
        {"id": 6, "_name": "name3"},
    ],
)
stmt = users.update().where(users.c.name == "jack").values(name="ed")

conn.execute(stmt)
# UPDATE users SET name=? WHERE users.name = ?
# ('ed', 'jack')
# COMMIT

result = conn.execute(users.delete().where(users.c.name == "jack"))
result.rowcount


conn.close()
