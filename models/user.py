from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False) 

    phones = relationship(
        "Phone",
        back_populates="user",
        cascade="all, delete-orphan"
    )