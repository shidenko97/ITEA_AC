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
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import create_database, drop_database, database_exists

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
db_name = "sqlalchemy_orm_db"
db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(db_url, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship(
        "Address",
        back_populates='user',
        cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"


User.__table__


def recreate_db(db_url):
    if database_exists(url=db_url):
        drop_database(url=db_url)
    create_database(url=db_url)


def create_tables(Base, engine):
    Base.metadata.create_all(engine)


def main():
    recreate_db(db_url=db_url)
    create_tables(Base, engine)


if __name__ == "__main__":
    main()
