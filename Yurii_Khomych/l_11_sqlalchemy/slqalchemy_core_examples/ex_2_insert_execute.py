from ex_1_define_and_create_tables_core import (
    users,
    addresses,
    engine,
)

ins = users.insert()
str(ins)
ins = users.insert().values(name="jack", fullname="Jack Jones")
str(ins)
ins.compile().params

conn = engine.connect()

result = conn.execute(ins)
# INSERT INTO users (name, fullname) VALUES (?, ?)
# ('jack', 'Jack Jones')
# COMMIT
ins.bind = engine
# str(ins)
result.inserted_primary_key

# conn.execute(ins, id=2, name='wendy', fullname='Wendy Williams')

conn.execute(
    addresses.insert(),
    [
        {"user_id": 1, "email_address": "jack@yahoo.com"},
        {"user_id": 1, "email_address": "jack@msn.com"},
        {"user_id": 2, "email_address": "www@www.org"},
        {"user_id": 2, "email_address": "wendy@aol.com"},
    ],
)
# INSERT INTO addresses (user_id, email_address) VALUES (?, ?)
# ((1, 'jack@yahoo.com'), (1, 'jack@msn.com'), (2, 'www@www.org'), (2, 'wendy@aol.com'))
# COMMIT

conn.close()
