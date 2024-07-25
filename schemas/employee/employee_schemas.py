import datetime
from pydantic import BaseModel, Field

class EmployeeBase(BaseModel):
    employee_id: str = Field(..., example="EMP123")
    job_title: str
    department: str
    salary: int
    dateIn: datetime.date
    dateOut: datetime.date | None = None  # Optional

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    comments: str | None = None

    class Config:
        orm_mode = True  # Para trabajar con objetos SQLAlchemy