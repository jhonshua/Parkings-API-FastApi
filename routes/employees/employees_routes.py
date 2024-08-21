from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Body
from schemas.employee.employee_schemas import   Response,EmployeeSchema
from controllers.employee.employee_controller import get_all_employee, create_employee
from config.db_config import SessionLocal
from middleware.validation.authenticate_user import authenticate_user

#----------------------------------------------------------------------------------------------

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#----------------------------------------------------------------------------------------------
# Retorna todos los employee 
@router.get("/")

async def get_all_employee_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(authenticate_user)):
    try:
        employees = get_all_employee(db, skip=skip, limit=limit)
        if not employees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No employe found in the database."
            )

        # Procesar los valores antes de incluirlos en la respuesta
        employee_dicts = [
            {
                'id': employee.id,
                'user_id': employee.user_id,
                "last_name": employee.last_name,
                "birth_date": employee.birth_date,
                "address": employee.address,
                "phone_number": employee.phone_number,
                "email": employee.email,
                "job_title": employee.job_title,
                "department": employee.department,
                "salary": employee.salary,
                "dateIn": employee.dateIn,  
                "emergency_contact_name": employee.emergency_contact_name,
                "emergency_contact_relationship": employee.emergency_contact_relationship,
                "emergency_contact_phone_number": employee.emergency_contact_phone_number
            }
            for employee in employees
        ]

        return Response(status="Ok", code="200", message="successfully", result = employee_dicts)

    except Exception as e:
        # Manejar la excepción aquí (puedes personalizar el mensaje de error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving rol data: {str(e)}"
        )
#---------------------------------------------------------------------------------------------- 
# Retorna un rol específico por ID
#@router.get("/{employee_id}")




#----------------------------------------------------------------------------------------------
# Crear un employee
@router.post("/")
async def create_employee_data(body_data= Body(...), db: Session = Depends(get_db), token: str = Depends(authenticate_user)):
    employee_data = EmployeeSchema(**body_data)
    try:
        create_employee(db, employee_data)
        return Response(status="Ok", 
                        code="200", 
                        message="created successfully").dict(exclude_none=True)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating employee: {str(e)}"
        )

#----------------------------------------------------------------------------------------------
# Actualizar un rol por ID
#@router.put("/{employee_id}")

#---------------------------------------------------------------------------------------------- 
# Eliminar un rol por ID
#@router.delete("/{employee_id}")