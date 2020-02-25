import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#
# conn = psycopg2.connect(
#     dbname='postgres',
#     user='postgres',
#     password='postgres',
#     host='localhost',
# )
# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor.execute('create database my_shop')
conn = psycopg2.connect(
    dbname="my_shop", user="postgres", password="postgres", host="localhost",
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("drop table if exists customers cascade")
# conn.commit()
# conn.rollback()
cursor.execute(
    """
create table customers
(
    id            serial primary key,
    customer_name varchar,
    contact_name  varchar,
    address       varchar,
    city          varchar,
    postal_code   varchar,
    country       varchar
)"""
)
cursor.execute(
    """
insert into customers (customer_name,
                       contact_name,
                       address,
                       city,
                       postal_code,
                       country)
values ('Alfreds Futterkiste ', 'Maria Anders',
        'Obere Str. 57', 'Berlin', '12209',
        'Germany');
"""
)

customers = (
    (
        "Alfreds Futterkiste ",
        "Maria Anders",
        "Obere Str. 57",
        "Berlin",
        "12209",
        "Germany",
    ),
    (
        "Ana Trujillo Emparedados",
        " Ana Trujillo",
        "Avda. de la Constitución 2222",
        "México",
        "D.F. 05021",
        "Mexico",
    ),
    (
        "Antonio Moreno Taquería",
        "Antonio Moreno",
        "Mataderos 2312",
        "México",
        "D.F. 05023",
        "Mexico",
    ),
)


cursor.execute("""select * from customers""")
for row in cursor:
    print(row)
with conn:
    query = """insert into customers (customer_name,
                           contact_name,
                           address,
                           city,
                           postal_code,
                           country)
    values (%s, %s, %s, %s, %s, %s)"""
    cursor.executemany(query, customers)
    cursor.execute("update customers set city=%s where id=%s", ("Kyiv", 1))
    cursor.rowcount
cursor.close()
conn.close()
#
from contextlib import closing
# with closing(psycopg2.connect(...)) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute('SELECT * FROM table_name LIMIT 5')
#         for row in cursor:
#             print(row)
#
# from psycopg2.extras import DictCursor
# with psycopg2.connect(...) as conn:
#     with conn.cursor(cursor_factory=DictCursor) as cursor:
#         pass

# cursor.fetchone()
# cursor.fetchall()
# cursor.fetchmany(size=5)


def create_db(cursor, db_name):
    query = f"create database {db_name}"
    cursor.execute(query)


def create_table(cursor, query):
    cursor.execute(query)


def create_product(name):
    query = "insert into product (name) values %s"


def main():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
    )
    with closing(psycopg2.connect(...)) as conn:
        with conn.cursor() as cursor:
            create_db(cursor, db_name="my_db")


if __name__ == "__main__":
    main()

pass
