from Serhii_Hidenko.l_9_sql.hw.params import DB_NAME, DB_USERNAME, DB_PASSWORD
from Serhii_Hidenko.l_9_sql.hw.postgre_connector import PostgreConnector


if __name__ == "__main__":

    with PostgreConnector(DB_USERNAME, DB_PASSWORD, DB_NAME) as db_conn:

        db_conn.execute("""
            SELECT
                ShipperName
            FROM
                Shippers
            WHERE
                ShipperID >= 1
        """)

        print(db_conn.fetchall())

        db_conn.execute("""
            SELECT
                COUNT(CategoryID)
            FROM
                Categories
            WHERE
                CategoryName LIKE 'Random %'
        """)

        print(db_conn.fetchone())

        db_conn.execute("""
            SELECT
                *
            FROM
                Employees
            WHERE
                Birthdate < NOW()
            ORDER BY
                Birthdate DESC
            LIMIT
                1
        """)

        print(db_conn.fetchone())
