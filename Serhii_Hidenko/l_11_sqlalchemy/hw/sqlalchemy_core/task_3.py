from sqlalchemy import or_, and_
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
        category_table.update().
        values(description="Updated description").
        where(category_table.c.category_name.like("%category%"))
    )

    conn.execute(
        customer_table.update().
        values(postal_code="Updated code", country="Neverland").
        where(customer_table.c.city.contains("city"))
    )

    conn.execute(
        employee_table.update().
        values(last_name="First id").
        where(
            or_(
                employee_table.c.id == 1,
                employee_table.c.id == 2,
            )
        )
    )

    conn.execute(
        order_detail_table.update().
        values(quantity=order_detail_table.c.quantity * 2).
        where(
            order_detail_table.c.quantity < 5
        )
    )

    conn.execute(
        order_table.update().
        values(employee_id=2).
        where(
            and_(
                order_table.c.id == 1,
                order_table.c.customer_id == 1,
            )
        )
    )

    conn.execute(
        product_table.update().
        values(unit=product_table.c.unit + "x2")
    )

    conn.execute(
        shipper_table.update().
        values(shipper_name="Updated " + shipper_table.c.phone).
        where(
            shipper_table.c.phone.like("%core _")
        )
    )

    conn.execute(
        supplier_table.update().
        values(address=supplier_table.c.phone + supplier_table.c.postal_code).
        where(
            and_(
                supplier_table.c.city.like("%city%"),
                supplier_table.c.country.like("%country%"),
            )
        )
    )

    conn.close()
