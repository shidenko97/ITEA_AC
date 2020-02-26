from datetime import datetime
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

    # Insert data to DB and save it
    session.add_all(
        [
            Categories(
                category_name="Category name orm 1",
                description="Category description orm 1"
            ),
            Categories(
                category_name="Category name orm 2",
                description="Category description orm 2"
            ),
            Customers(
                customer_name="Customer name orm 1",
                contact_name="Customer contact name orm 1",
                address="Customer address orm 1",
                city="Customer city orm 1",
                postal_code="Postalcode orm 1",
                country="Customer country orm 1",
            ),
            Customers(
                customer_name="Customer name orm 2",
                contact_name="Customer contact name orm 2",
                address="Customer address orm 2",
                city="Customer city orm 2",
                postal_code="Postalcode orm 2",
                country="Customer country orm 2",
            ),
            Employees(
                last_name="Employee last name orm 1",
                first_name="Employee first name orm 1",
                birth_date=datetime(2020, 2, 25),
                photo="Employee photo orm 1",
                notes="Employee notes orm 1",
            ),
            Employees(
                last_name="Employee last name orm 2",
                first_name="Employee first name orm 2",
                birth_date=datetime(2020, 2, 26),
                photo="Employee photo orm 2",
                notes="Employee notes orm 2",
            ),
            Shippers(
                shipper_name="Shipper name orm 1",
                phone="Phone orm 1",
            ),
            Shippers(
                shipper_name="Shipper name orm 2",
                phone="Phone orm 2",
            ),
            Suppliers(
                supplier_name="Supplier name orm 1",
                contact_name="Supplier contact name orm 1",
                address="Supplier address orm 1",
                city="Supplier city orm 1",
                postal_code="Postalcode orm 1",
                country="Supplier country orm 1",
                phone="Phone orm 1",
            ),
            Suppliers(
                supplier_name="Supplier name orm 2",
                contact_name="Supplier contact name orm 2",
                address="Supplier address orm 2",
                city="Supplier city orm 2",
                postal_code="Postalcode orm 2",
                country="Supplier country orm 2",
                phone="Phone orm 2",
            ),
        ]
    )

    session.commit()

    session.add_all(
        [
            Orders(
                customer_id=1,
                employee_id=1,
                order_date=datetime(2020, 2, 25),
                shipper_id=1
            ),
            Orders(
                customer_id=2,
                employee_id=2,
                order_date=datetime(2020, 2, 26),
                shipper_id=2
            ),
            Products(
                product_name="Product unit orm 1",
                supplier_id=1,
                category_id=1,
                unit="Product unit orm 1",
                price=1.1
            ),
            Products(
                product_name="Product unit orm 2",
                supplier_id=2,
                category_id=2,
                unit="Product unit orm 2",
                price=2.2
            ),
        ]
    )

    session.commit()

    session.add(OrderDetails(order_id=1, product_id=1, quantity=1))
    session.add(OrderDetails(order_id=2, product_id=2, quantity=2))

    session.commit()
