from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from config.db_config import Base 

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"))  
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column( Date)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    job_title = Column(String)
    department = Column(String)
    salary = Column(Integer)
    dateIn = Column(DateTime, nullable=True)
    dateOut = Column(DateTime, nullable=True)
    comments = Column(Text, nullable=True)  
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_relationship = Column(String, nullable=True)  
    emergency_contact_phone_number = Column(String, nullable=True)

 # Optional: Define a relationship with User
   #  user = relationship("User", back_populates="employee")
    
