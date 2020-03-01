from sqlalchemy import select
import os
from Serhii_Hidenko.l_11_sqlalchemy.hw.sqlalchemy_core.task_1 import MyDb,\
    category_table, supplier_table, product_table


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

    with engine.connect() as conn:

        print(
            conn.execute(
                select(
                    [
                        category_table.c.category_name
                    ]
                )
            ).fetchone()
        )

        print(
            conn.execute(
                select(
                    [
                        supplier_table.c.supplier_name
                    ]
                ).where(
                    supplier_table.c.city.like("%city%")
                ).
                group_by(supplier_table.c.id).
                having(supplier_table.c.id > 0)
            ).fetchall()
        )

        print(
            conn.execute(
                select(
                    [
                        product_table.c.product_name,
                        category_table.c.category_name
                    ]
                ).
                select_from(product_table.join(category_table)).
                where(category_table.c.id > 0).
                order_by(product_table.c.product_name.desc())
            ).fetchall()[:3]
        )

        print(
            conn.execute(
                select(
                    [
                        product_table.c.product_name,
                        category_table.c.category_name
                    ]
                ).
                where(category_table.c.id > 0).
                distinct(category_table.c.category_name)
            ).fetchall()
        )
