import os
from sqlalchemy import Column, Integer, String, Text, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Serhii_Hidenko.l_11_sqlalchemy.hw.my_db import MyDb


Base = declarative_base()


class Customers(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(64))
    contact_name = Column(String(64))
    address = Column(String(64))
    city = Column(String(32))
    postal_code = Column(String(16))
    country = Column(String(32))

    def __repr__(self):
        return f"<Customers({self.customer_name})>"


class Categories(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    category_name = Column(String(64))
    description = Column(Text)

    products = relationship(
        "Products", back_populates="category"
    )

    def __repr__(self):
        return f"<Categories({self.category_name})>"


class Employees(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(64))
    first_name = Column(String(64))
    birth_date = Column(Date)
    photo = Column(String(128))
    notes = Column(Text)

    def __repr__(self):
        return f"<Employees({self.first_name} {self.last_name})>"


class OrderDetails(Base):

    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer)

    def __repr__(self):
        return f"<OrderDetails({self.id})>"


class Orders(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id",
                                             ondelete="CASCADE"))
    employee_id = Column(Integer, ForeignKey("employees.id",
                                             ondelete="CASCADE"))
    order_date = Column(Date)
    shipper_id = Column(Integer, ForeignKey("shippers.id",
                                            ondelete="CASCADE"))

    def __repr__(self):
        return f"<Orders({self.id})>"


class Products(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_name = Column(String(64))
    supplier_id = Column(Integer, ForeignKey("suppliers.id",
                                             ondelete="CASCADE"))
    category_id = Column(Integer, ForeignKey("categories.id",
                                             ondelete="CASCADE"))
    unit = Column(String(32))
    price = Column(Numeric("10,2"))

    category = relationship(
        "Categories", back_populates="products"
    )

    def __repr__(self):
        return f"<Products({self.product_name})>"


class Shippers(Base):

    __tablename__ = "shippers"

    id = Column(Integer, primary_key=True)
    shipper_name = Column(String(64))
    phone = Column(String(16))

    def __repr__(self):
        return f"<Shippers({self.shipper_name})>"


class Suppliers(Base):

    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    supplier_name = Column(String(64))
    contact_name = Column(String(64))
    address = Column(String(64))
    city = Column(String(64))
    postal_code = Column(String(16))
    country = Column(String(32))
    phone = Column(String(16))

    def __repr__(self):
        return f"<Suppliers({self.supplier_name})>"


if __name__ == "__main__":

    db = MyDb.create(
        username=os.environ.get("PG_USERNAME"),
        password=os.environ.get("PG_PASSWORD"),
        hostname=os.environ.get("PG_HOSTNAME"),
        database=os.environ.get("PG_DATABASE"),
        port=os.environ.get("PG_PORT")
    )

    # Create all initiated tables
    db.create_tables(base=Base)
