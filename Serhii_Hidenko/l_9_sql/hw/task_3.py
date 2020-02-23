from Serhii_Hidenko.l_9_sql.hw.params import DB_NAME, DB_USERNAME, DB_PASSWORD
from Serhii_Hidenko.l_9_sql.hw.postgre_connector import PostgreConnector


if __name__ == "__main__":

    with PostgreConnector(DB_USERNAME, DB_PASSWORD, DB_NAME) as db_conn:

        # Insert data into table Customers
        db_conn.execute("""
            INSERT INTO
                Customers (
                    CustomerName,
                    ContactName,
                    Address,
                    City,
                    PostalCode,
                    Country
                ) VALUES (
                    'Customer 1',
                    'Contact 1',
                    'Address 1',
                    'City 1',
                    'Postal 1',
                    'Country 1'
                ), (
                    'Customer 2',
                    'Contact 2',
                    'Address 2',
                    'City 2',
                    'Postal 2',
                    'Country 2'
                ), (
                    'Customer 3',
                    'Contact 3',
                    'Address 3',
                    'City 3',
                    'Postal 3',
                    'Country 3'
                );
        """)

        # Insert data into table Categories
        db_conn.execute("""
            INSERT INTO
                Categories (
                    CategoryName,
                    Description
                ) VALUES (
                    'Category 1',
                    'Description category 1'
                ), (
                    'Category 2',
                    'Description category 2'
                ), (
                    'Category 3',
                    'Description category 3'
                );
        """)

        # Insert data into table Employees
        db_conn.execute("""
            INSERT INTO
                Employees (
                    LastName,
                    FirstName,
                    BirthDate,
                    Photo,
                    Notes
                ) VALUES (
                    'LastName 1',
                    'FirstName 1',
                    '2000-01-01',
                    'Photo 1',
                    'Notes 1'
                ), (
                    'LastName 2',
                    'FirstName 2',
                    '2001-01-01',
                    'Photo 2',
                    'Notes 2'
                ), (
                    'LastName 3',
                    'FirstName 3',
                    '2010-01-01',
                    'Photo 3',
                    'Notes 3'
                );
        """)

        # Insert data into table Shippers
        db_conn.execute("""
            INSERT INTO
                Shippers (
                    ShipperName,
                    Phone
                ) VALUES (
                    'ShipperName 1',
                    'Phone 1'
                ), (
                    'ShipperName 2',
                    'Phone 2'
                ), (
                    'ShipperName 3',
                    'Phone 3'
                );
        """)

        # Insert data into table Suppliers
        db_conn.execute("""
            INSERT INTO
                Suppliers (
                    SupplierName,
                    ContactName,
                    Address,
                    City,
                    PostalCode,
                    Country,
                    Phone
                ) VALUES (
                    'SupplierName 1',
                    'ContactName 1',
                    'Address 1',
                    'City 1',
                    'PostalCode 1',
                    'Country 1',
                    'Phone 1'
                ), (
                    'SupplierName 2',
                    'ContactName 2',
                    'Address 2',
                    'City 2',
                    'PostalCode 2',
                    'Country 2',
                    'Phone 2'
                ), (
                    'SupplierName 3',
                    'ContactName 3',
                    'Address 3',
                    'City 3',
                    'PostalCode 3',
                    'Country 3',
                    'Phone 3'
                );
        """)

        # Insert data into table Orders
        db_conn.execute("""
            INSERT INTO
                Orders (
                    CustomerID,
                    EmployeeID,
                    OrderDate,
                    ShipperID
                ) VALUES (
                    1,
                    1,
                    '2020-02-22',
                    1
                ), (
                    2,
                    2,
                    '2020-02-21',
                    2
                ), (
                    3,
                    3,
                    '2020-02-20',
                    3
                );
        """)

        # Insert data into table Products
        db_conn.execute("""
            INSERT INTO
                Products (
                    ProductName,
                    SupplierID,
                    CategoryID,
                    Unit,
                    Price
                ) VALUES (
                    'ProductName 1',
                    1,
                    1,
                    '1 piece',
                    10.2
                ), (
                    'ProductName 2',
                    2,
                    2,
                    '2 piece',
                    10.3
                ), (
                    'ProductName 3',
                    3,
                    3,
                    '3 piece',
                    13.2
                );
        """)

        # Insert data into table OrderDetails
        db_conn.execute("""
            INSERT INTO
                OrderDetails (
                    OrderID,
                    ProductID,
                    Quantity
                ) VALUES (
                    1,
                    1,
                    1
                ), (
                    2,
                    2,
                    2
                ), (
                    3,
                    3,
                    3
                );
        """)
