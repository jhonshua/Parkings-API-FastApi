from sqlalchemy.orm import Session
from models.employees.employee_model import Employee
from schemas.employee.employee_schemas import EmployeeSchema



#-------------------------------------------------------------------------------------------
#todos los employee
def get_all_employee(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(Employee).offset(skip).limit(limit).all()
    return roles

#-------------------------------------------------------------------------------------------
#creamos empleado
def create_employee(db: Session, employee_data: EmployeeSchema):
    
    _employee = Employee(
        user_id = employee_data.user_id,
        first_name = employee_data.first_name,
        last_name = employee_data.last_name,
        birth_date = employee_data.birth_date,
        address = employee_data.address,
        phone_number=employee_data.phone_number,
        email = employee_data.email,
        job_title = employee_data.job_title,
        department = employee_data.department,
        salary = employee_data.salary,
        dateIn = employee_data.dateIn,
        emergency_contact_name = employee_data.emergency_contact_name,
        emergency_contact_relationship = employee_data.emergency_contact_relationship,
        emergency_contact_phone_number = employee_data.emergency_contact_phone_number
    )
    db.add(_employee)
    db.commit()
    db.refresh(_employee) 
    
    return _employee