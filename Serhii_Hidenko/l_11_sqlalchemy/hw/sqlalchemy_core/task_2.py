from datetime import datetime
from Serhii_Hidenko.l_11_sqlalchemy.hw.sqlalchemy_core.task_1 import *


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

    conn = engine.connect()

    conn.execute(
        category_table.insert(),
        [
            {
                "category_name": "Category name core 1",
                "description": "Category description core 1"
            },
            {
                "category_name": "Category name core 2",
                "description": "Category description core 2"
            },
        ],
    )

    conn.execute(
        customer_table.insert(),
        [
            {
                "customer_name": "Customer name core 1",
                "contact_name": "Customer contact name core 1",
                "address": "Customer address core 1",
                "city": "Customer city core 1",
                "postal_code": "Post code core 1",
                "country": "Customer country core 1",
            },
            {
                "customer_name": "Customer name core 2",
                "contact_name": "Customer contact name core 2",
                "address": "Customer address core 2",
                "city": "Customer city core 2",
                "postal_code": "Post code core 2",
                "country": "Customer country core 2",
            },
        ],
    )

    conn.execute(
        employee_table.insert(),
        [
            {
                "last_name": "Employee last name core 1",
                "first_name": "Employee first name core 1",
                "birth_date": datetime(2020, 2, 25),
                "photo": "Employee photo core 1",
                "notes": "Employee notes core 1",
            },
            {
                "last_name": "Employee last name core 2",
                "first_name": "Employee first name core 2",
                "birth_date": datetime(2020, 2, 26),
                "photo": "Employee photo core 2",
                "notes": "Employee notes core 2",
            },
        ],
    )

    conn.execute(
        shipper_table.insert(),
        [
            {
                "shipper_name": "Shipper name core 1",
                "phone": "Phone core 1",
            },
            {
                "shipper_name": "Shipper name core 2",
                "phone": "Phone core 2",
            },
        ],
    )

    conn.execute(
        supplier_table.insert(),
        [
            {
                "supplier_name": "Supplier name core 1",
                "contact_name": "Supplier contact name core 1",
                "address": "Supplier address core 1",
                "city": "Supplier city core 1",
                "postal_code": "Post code core 1",
                "country": "Supplier country core 1",
                "phone": "Phone core 1",
            },
            {
                "supplier_name": "Supplier name core 2",
                "contact_name": "Supplier contact name core 2",
                "address": "Supplier address core 2",
                "city": "Supplier city core 2",
                "postal_code": "Post code core 2",
                "country": "Supplier country core 2",
                "phone": "Phone core 2",
            },
        ],
    )

    conn.execute(
        order_table.insert(),
        [
            {
                "customer_id": 1,
                "employee_id": 1,
                "order_date": datetime(2020, 2, 25),
                "shipper_id": 1
            },
            {
                "customer_id": 2,
                "employee_id": 2,
                "order_date": datetime(2020, 2, 26),
                "shipper_id": 2
            },
        ],
    )

    conn.execute(
        product_table.insert(),
        [
            {
                "product_name": "Product unit core 1",
                "supplier_id": 1,
                "category_id": 1,
                "unit": "Product unit core 1",
                "price": 1.1
            },
            {
                "product_name": "Product unit core 2",
                "supplier_id": 2,
                "category_id": 2,
                "unit": "Product unit core 2",
                "price": 2.2
            },
        ],
    )

    conn.execute(
        order_detail_table.insert(),
        [
            {
                "order_id": 1,
                "product_id": 1,
                "quantity": 1
            },
            {
                "order_id": 2,
                "product_id": 2,
                "quantity": 2
            },
        ],
    )

    conn.close()
