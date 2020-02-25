# pip install sqlalchemy
# pip install sqlalchemy-utils
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
)
from sqlalchemy_utils import create_database, drop_database, database_exists

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
db_name = "sqlalchemy_core_db"
db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(db_url, echo=True)

metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String,),
    Column("fullname", String),
)
addresses = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", None, ForeignKey("users.id")),
    Column("email_address", String, nullable=False),
)


def recreate_db(db_url):
    if database_exists(url=db_url):
        drop_database(url=db_url)
    create_database(url=db_url)


def create_tables(engine, metadata):
    metadata.create_all(engine)


def main():
    recreate_db(db_url=db_url)
    create_tables(engine=engine, metadata=metadata)


if __name__ == "__main__":
    main()
