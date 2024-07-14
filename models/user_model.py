from sqlalchemy import  Column, Integer, String, Text
from config.db_config import Base  # Assuming your declarative base class is here

class User(Base):
    # Name of the table in the database
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(Text, nullable=True)  # Allows for longer phone numbers
    status = Column(String)
    rol_id = Column(String)
    ability = Column(Text)
