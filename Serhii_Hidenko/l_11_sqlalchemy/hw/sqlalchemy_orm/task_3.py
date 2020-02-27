from sqlalchemy import or_, and_
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

    session.\
        query(Categories).\
        filter(Categories.id == 1).\
        update({
            "category_name": "Category updated by orm"
        })

    session. \
        query(Customers). \
        filter(Customers.postal_code == "Updated code"). \
        update({
            "postal_code": "02090"
        })

    session. \
        query(Employees). \
        filter(
            or_(
                Employees.notes == "",
                Employees.notes == "Employee notes core 2"
            )
        ).update({
            "photo": "wow_photo.png"
        })

    session. \
        query(OrderDetails). \
        filter(
            and_(
                OrderDetails.order_id == 1,
                OrderDetails.product_id == 1
            )
        ).update({
            "quantity": 20
        })

    session. \
        query(Orders). \
        update({
            "shipper_id": 1
        })

    session. \
        query(Products). \
        filter(
            Products.price >= 2
        ).update({
            "unit": 100,
            "price": 0
        })

    session. \
        query(Shippers). \
        filter(
            Shippers.phone == ""
        ).update({
            "shipper_name": "My phone"
        })

    session. \
        query(Suppliers). \
        filter(
            Suppliers.country == "Ukraine"
        ).update({
            "city": Suppliers.postal_code
        })

    session.commit()

    session.close()
