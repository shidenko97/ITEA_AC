from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from models import Base, Department, Employee

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
db_name = "alembic_db"
db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(db_url, echo=True)

session = sessionmaker()
session.configure(bind=engine)
# Base.metadata.bind = engine
s = session()
IT = Department(name="IT")
Financial = Department(name="Financial")
s.add(IT)
s.add(Financial)
cathy = Employee(name="Cathy")
marry = Employee(name="Marry")
john = Employee(name="John")
s.add(cathy)
s.add(marry)
s.add(john)
cathy.departments.append(Financial)
marry.departments.append(Financial)
john.departments.append(IT)
s.commit()
s.close()
