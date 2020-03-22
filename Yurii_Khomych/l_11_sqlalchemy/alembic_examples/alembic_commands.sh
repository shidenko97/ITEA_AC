pip install alembic
alembic init alembic
# Change the line thats starts with "sqlalchemy.url" into "sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/alembic_db”
# sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
# set to target_metadata = Base.metadata
export PYTHONPATH=.
alembic current
alembic revision -m "initial tables" --autogenerate
alembic upgrade head
alembic revision -m "add department_employee_link" --autogenerate
alembic upgrade head
alembic current