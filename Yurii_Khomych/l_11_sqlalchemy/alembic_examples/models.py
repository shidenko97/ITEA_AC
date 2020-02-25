from sqlalchemy import (
    Integer,
    String,
    Column,
    DateTime,
    func,
    create_engine,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())


class DepartmentEmployeeLink(Base):
    __tablename__ = "department_employee_link"
    department_id = Column(
        Integer, ForeignKey("department.id"), primary_key=True
    )
    employee_id = Column(Integer, ForeignKey("employee.id"), primary_key=True)
