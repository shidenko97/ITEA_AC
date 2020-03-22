from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ex_1_define_and_create_tables_orm import User, Base, engine, create_tables


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user"
)

if __name__ == "__main__":
    create_tables(Base=Base, engine=engine)
