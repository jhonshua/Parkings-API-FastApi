from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar
import datetime

T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None  

class EmployeeSchema(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    birth_date: str  # Optional for flexibility
    address: str
    phone_number: int
    email: str
    job_title: str
    department: str
    salary: int
    dateIn: datetime.datetime  # Assuming datetime storage
    dateOut: Optional[datetime.datetime] = None
    comments: Optional[str] = None
    emergency_contact_name : str
    emergency_contact_relationship : str
    emergency_contact_phone_number : int

    class Config:
        orm_mode = True  # Enable working with SQLAlchemy objects
        
