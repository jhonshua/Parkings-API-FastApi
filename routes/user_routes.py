from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from controllers.user_controller import get_all_users, create_user, get_user, update_user, delete_user
from config.db_config import SessionLocal
from schemas.user_schemas import  Response


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Retorna todos los usuarios
@router.get("/")
async def get_all_users_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_all_users(db, skip=skip, limit=limit)
    if not users:  # Check if the list of users is empty
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found in the database."
        ) 
    
    return Response(status="Ok",
                      code="200",
                      message="successfully", result = users)


# Retorna un usuario específico por ID
@router.get("/{user_id}")
def get_single_user(user_id: int):
    return get_user(user_id)

# Crear un usuario
@router.post("/", status_code=201)
def create_single_user(user_data: dict):
    return create_user(user_data)

# Actualizar un usuario por ID
@router.put("/{user_id}", status_code=202)
def update_single_user(user_id: int, new_data: dict):
    return update_user(user_id, new_data)

# Eliminar un usuario por ID
@router.delete("/{user_id}")
async def delete_single_user(user_id: int, db: Session = Depends(get_db)):
    print(user_id)
    deletion_successful = delete_user(db, user_id)

    if deletion_successful:
        return Response(status="Ok",
                          code="200",
                          message="User deleted successfully")
    else:
        return Response(status="Error",
                          code="404",  
                          message="User deletion failed")

