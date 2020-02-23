from Serhii_Hidenko.l_9_sql.hw.params import DB_NAME, DB_USERNAME, DB_PASSWORD
from Serhii_Hidenko.l_9_sql.hw.postgre_connector import PostgreConnector


if __name__ == "__main__":

    with PostgreConnector(DB_USERNAME, DB_PASSWORD, DB_NAME) as db_conn:

        # Update data into table Customers
        db_conn.execute("""
            UPDATE
                Customers
            SET
                CustomerName = 'Random customer',
                ContactName = 'Random contact'
            WHERE
                CustomerID >= 2
        """)

        # Update data into table Categories
        db_conn.execute("""
            UPDATE
                Categories  
            SET
                CategoryName = 'Random category'
            WHERE
                CategoryID != 2
        """)

        # Update data into table Employees
        db_conn.execute("""
            UPDATE
                Employees
            SET
                FirstName = 'Random FirstName'
            WHERE
                EmployeeID <= 2
        """)

        # Update data into table Shippers
        db_conn.execute("""
            UPDATE
                Shippers
            SET
                ShipperName = 'Random shipper'
            WHERE
                ShipperID != 1
        """)

        # Update data into table Suppliers
        db_conn.execute("""
            UPDATE
                Suppliers
            SET
                SupplierName = 'Random supplier'
            WHERE
                SupplierID > 0
        """)

        # Update data into table Orders
        db_conn.execute("""
            UPDATE
                Orders
            SET
                EmployeeID = 1
            WHERE
                EmployeeID = 2
        """)

        # Update data into table Products
        db_conn.execute("""
            UPDATE
                Products
            SET
                CategoryID = 3
            WHERE
                ProductID = 2
        """)

        # Update data into table OrderDetails
        db_conn.execute("""
            UPDATE
                OrderDetails
            SET
                Quantity = 33
        """)
