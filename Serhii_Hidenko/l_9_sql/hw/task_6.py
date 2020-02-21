from Serhii_Hidenko.l_9_sql.hw.params import DB_NAME, DB_USERNAME, DB_PASSWORD
from Serhii_Hidenko.l_9_sql.hw.postgre_connector import PostgreConnector


if __name__ == "__main__":

    with PostgreConnector(DB_USERNAME, DB_PASSWORD, DB_NAME) as db_conn:

        db_conn.execute("""
            SELECT
                Orders.Orderdate,
                Shippers.ShipperName
            FROM
                Shippers
            LEFT JOIN
                Orders
            ON
                Orders.ShipperID = Shippers.ShipperID
            WHERE
                Orders.OrderID = 1
        """)

        print(db_conn.fetchall())

        db_conn.execute("""
            SELECT
                Products.ProductName,
                Categories.CategoryName
            FROM
                Products
            LEFT JOIN
                Categories
            ON
                Categories.CategoryID = Products.ProductID
            ORDER BY
                Products.ProductName DESC
            LIMIT 1       
        """)

        print(db_conn.fetchone())

        db_conn.execute("""
            SELECT
                *
            FROM
                Orders
            LEFT JOIN
                Customers
            ON
                Customers.CustomerID = Orders.OrderID
            LEFT JOIN
                Employees
            ON
                Employees.EmployeeID = Orders.EmployeeID
            LEFT JOIN
                Shippers
            ON
                Shippers.ShipperID = Orders.ShipperID
            LEFT JOIN
                OrderDetails
            ON
                OrderDetails.OrderDetailID = Orders.OrderID
            LEFT JOIN
                Products
            ON
                Products.ProductID = OrderDetails.ProductID
            LEFT JOIN
                Categories
            ON
                Categories.CategoryID = Products.CategoryID
            LEFT JOIN
                Suppliers
            ON
                Suppliers.SupplierID = Products.SupplierID
        """)

        print(db_conn.fetchall())
