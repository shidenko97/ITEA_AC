from sqlalchemy import or_, and_
import os
from Serhii_Hidenko.l_11_sqlalchemy.hw.sqlalchemy_core.task_1 import MyDb,\
    category_table, customer_table, employee_table, shipper_table,\
    supplier_table, order_table, product_table, order_detail_table


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
        category_table.delete().
        where(category_table.c.category_name.like("%category%"))
    )

    conn.execute(
        customer_table.delete().
        where(customer_table.c.city.contains("city"))
    )

    conn.execute(
        employee_table.delete().
        where(
            or_(
                employee_table.c.id == 1,
                employee_table.c.id == 2,
            )
        )
    )

    conn.execute(
        order_detail_table.delete().
        where(
            order_detail_table.c.quantity < 5
        )
    )

    conn.execute(
        order_table.delete().
        where(
            and_(
                order_table.c.id == 1,
                order_table.c.customer_id == 1,
            )
        )
    )

    conn.execute(
        product_table.delete()
    )

    conn.execute(
        shipper_table.delete().
        where(
            shipper_table.c.phone.like("%core _")
        )
    )

    conn.execute(
        supplier_table.delete().
        where(
            and_(
                supplier_table.c.city.like("%city%"),
                supplier_table.c.country.like("%country%"),
            )
        )
    )

    conn.close()
