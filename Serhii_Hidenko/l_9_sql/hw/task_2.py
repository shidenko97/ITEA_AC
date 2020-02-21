from Serhii_Hidenko.l_9_sql.hw.params import DB_NAME, DB_USERNAME, DB_PASSWORD
from Serhii_Hidenko.l_9_sql.hw.postgre_connector import PostgreConnector


if __name__ == "__main__":

    with PostgreConnector(DB_USERNAME, DB_PASSWORD) as db_conn:

        # Create database
        db_conn.execute(f"""
            SELECT
                'CREATE DATABASE {DB_NAME}' 
            WHERE 
                NOT EXISTS (
                    SELECT FROM 
                        pg_database 
                    WHERE 
                        pg_database.datname = '{DB_NAME}'
                );
        """)

    with PostgreConnector(DB_USERNAME, DB_PASSWORD, DB_NAME) as db_conn:

        # Create table Customers
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Customers (
                    CustomerID SERIAL,
                    CustomerName varchar(64),
                    ContactName varchar(32),
                    Address varchar(64),
                    City varchar(32),
                    PostalCode varchar(16),
                    Country varchar(32),
                    PRIMARY KEY (CustomerID)
                );
        """)

        # Create table Categories
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Categories (
                    CategoryID SERIAL,
                    CategoryName varchar(64),
                    Description text,
                    PRIMARY KEY (CategoryID)
                );
        """)

        # Create table Employees
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Employees (
                    EmployeeID SERIAL,
                    LastName varchar(32),
                    FirstName varchar(32),
                    BirthDate date,
                    Photo varchar(255),
                    Notes text,
                    PRIMARY KEY (EmployeeID)
                );
        """)

        # Create table Shippers
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Shippers (
                    ShipperID SERIAL,
                    ShipperName varchar(64),
                    Phone varchar(16),
                    PRIMARY KEY (ShipperID)
                );
        """)

        # Create table Suppliers
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Suppliers (
                    SupplierID SERIAL,
                    SupplierName varchar(64),
                    ContactName varchar(64),
                    Address varchar(32),
                    City varchar(32),
                    PostalCode varchar(16),
                    Country varchar(32),
                    Phone varchar(16),
                    PRIMARY KEY (SupplierID)
                );
        """)

        # Create table Orders
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Orders (
                    OrderID SERIAL,
                    CustomerID int REFERENCES Customers(CustomerID),
                    EmployeeID int REFERENCES Employees(EmployeeID),
                    OrderDate date,
                    ShipperID int REFERENCES Shippers(ShipperID),
                    PRIMARY KEY (OrderID)
                );
        """)

        # Create table Products
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                Products (
                    ProductID SERIAL,
                    ProductName varchar(128),
                    SupplierID int REFERENCES Suppliers(SupplierID),
                    CategoryID int REFERENCES Categories(CategoryID),
                    Unit varchar(64),
                    Price numeric(10, 2),
                    PRIMARY KEY (ProductID)
                );
        """)

        # Create table OrderDetails
        db_conn.execute("""
            CREATE TABLE IF NOT EXISTS
                OrderDetails (
                    OrderDetailID SERIAL,
                    OrderID int REFERENCES Orders(OrderID),
                    ProductID int REFERENCES Products(ProductID),
                    Quantity int,
                    PRIMARY KEY (OrderDetailID)
                );
        """)
