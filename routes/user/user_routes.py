from fastapi import APIRouter
from fastapi import  Depends, HTTPException, status,Body
from sqlalchemy.orm import Session
from controllers.user.user_controller import get_all_users, create_user, get_user, update_user, delete_user
from config.db_config import SessionLocal
from schemas.user.user_schemas import UserSchema,  Response, EmailSchema
from middleware.validation.authenticate_user import authenticate_user
from models.user.user_model import User
from utils.send_mail import send_email

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Retorna todos los usuarios
@router.get("/")
async def get_all_users_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(authenticate_user)):
    try:
        users = get_all_users(db, skip=skip, limit=limit)
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No users found in the database."
            )

        # Procesar los valores antes de incluirlos en la respuesta
        user_dicts = [
            {
                'id': user.id,
                'full_name': user.full_name.strip('"'),
                'username': user.username.strip('"'),
                'email': user.email.strip('"'),
                'password': user.password.strip('"'),
                'phone': user.phone.strip('"'),
                'status': user.phone.strip('"'),
                'rol_id': user.rol_id.strip('"'),
            }
            for user in users
        ]

        return Response(status="Ok", code="200", message="successfully", result=user_dicts)

    except Exception as e:
        # Manejar la excepción aquí (puedes personalizar el mensaje de error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving user data: {str(e)}"
        )

# Retorna un usuario específico por ID
@router.get("/{user_id}")

async def get_single_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(authenticate_user)):
    try: 
        user= get_user(db, user_id)
        
        user_dicts = [
            {
                'id': user.id,
                'full_name': user.full_name.strip('"'),
                'username': user.username.strip('"'),
                'email': user.email.strip('"'),
                'password': user.password.strip('"'),
                'phone': user.phone.strip('"'),
                'status': user.phone.strip('"'),
                'rol_id': user.rol_id.strip('"'),
            }
        ]
        
        return Response(status="Ok",
                          code="200",
                          message="User search successfully", result=user_dicts)
        
    except Exception as e:
        return Response(status="Error",
                          code="404",  
                          message=f"User search failed{str(e)}")
    

# Crear un usuario
@router.post("/")
async def create_single_user(body_data= Body(...), db: Session = Depends(get_db), current_user: User = Depends(authenticate_user)):
    user_data = UserSchema(**body_data)
    try:    
        create_user( db, user_data )
        data  = EmailSchema(
            email =   user_data.email,
            password =  user_data.password
           )
      
        await send_email(data)
        return Response(status="Ok", 
                        code="200", 
                        message="created successfully").dict(exclude_none=True)
    except Exception as e:
        return Response(status="Error ", code="500", message=str(e)).dict(exclude_none=True)
    
    
# Actualizar un usuario por ID
@router.put("/{user_id}")
async def update_single_user(user_id: int, current_user: User = Depends(authenticate_user),  body_data= Body(...), db: Session = Depends(get_db)):
    try:
        user = update_user(db, user_id, user_data=body_data)
        user_dicts = [
            { 
                'id': user.id,
                'full_name': user.full_name.strip('"'),
                'username': user.username.strip('"'),
                'email': user.email.strip('"'),
                'password': user.password.strip('"'),
                'phone': user.phone.strip('"'),
                'status': user.phone.strip('"'),
                'rol_id': user.rol_id.strip('"'),
            }
        ]
        
        return Response(status="Ok",
                          code="200",
                          message="User update successfully", result = user_dicts)
        
    except Exception as e:
        return Response(status="Error",
                          code="404",  
                          message=f"User update failed{str(e)}")


# Eliminar un usuario por ID

@router.delete("/{user_id}")
async def delete_single_user(user_id: int, current_user: User = Depends(authenticate_user), db: Session = Depends(get_db)):
    try:
        delete_user(db, user_id)
        return Response(status="Ok",
                        code="200",
                        message="User deleted successfully")
    except HTTPException as e:
        # Handle HTTP exceptions raised by the middleware or your logic
        return e
    except Exception as e:
        # Handle other unexpected errors
        return Response(status="Error",
                        code="404",
                        message=f"User deletion failed: {str(e)}")

