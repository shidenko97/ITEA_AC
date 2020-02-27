from sqlalchemy.orm import sessionmaker
from Serhii_Hidenko.l_11_sqlalchemy.hw.sqlalchemy_orm.task_1 import *


if __name__ == "__main__":

    # Initiate DB and engine
    db = MyDb.create(
        username=os.environ.get("PG_USERNAME"),
        password=os.environ.get("PG_PASSWORD"),
        hostname=os.environ.get("PG_HOSTNAME"),
        database=os.environ.get("PG_DATABASE"),
        port=os.environ.get("PG_PORT")
    )
    engine = db.engine

    # Initiate session
    Session = sessionmaker(bind=engine)
    session = Session()

    print(
        session.
        query(Categories.category_name).
        all()
    )

    print(
        session.
        query(Suppliers.postal_code).
        filter(
            Suppliers.city.like("%city%")
        ).
        group_by(Suppliers.id).
        having(Suppliers.id > 0).
        all()
    )

    print(
        session.
        query(
            Products.product_name,
            Categories.category_name
        ).
        join(Categories).
        filter(Categories.id > 0).
        order_by(Products.product_name.desc()).
        all()[:3]
    )

    print(
        session.
        query(
            Products.product_name,
            Categories.category_name
        ).
        filter(Categories.id > 0).
        distinct(Categories.category_name).
        all()
    )

    session.close()
