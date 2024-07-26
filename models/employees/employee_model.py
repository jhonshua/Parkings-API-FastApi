from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from config.db_config import Base 

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"))  
    job_title = Column(String)
    department = Column(String)
    salary = Column(Integer)
    dateIn = Column(DateTime, nullable=True)
    dateOut = Column(DateTime, nullable=True)
    comments = Column(Text, nullable=True)  

 # Optional: Define a relationship with User
   #  user = relationship("User", back_populates="employee")
    
