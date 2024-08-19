from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status,Body
from schemas.roles.roles_schemas import   Response 
from controllers.roles.roles_controller import get_all_rol, create_rol, delete_rol, get_rol, update_rol
from config.db_config import SessionLocal
from middleware.validation.authenticate_user import authenticate_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Retorna todos los roles
@router.get("/")
  
# Retorna un rol específico por ID
@router.get("/{employee_id}")

# Crear un rol
@router.post("/")

# Actualizar un rol por ID
@router.put("/{employee_id}")
 
# Eliminar un rol por ID
@router.delete("/{employee_id}")