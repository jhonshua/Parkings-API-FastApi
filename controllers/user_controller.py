from sqlalchemy.orm import Session
from models.user_model import User

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
   return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
     return db.query(User).filter(User.id == user_id).first()

def create_user(user_data: dict):
    # Lógica para crear un usuario en la base de datos
    # Por ejemplo, guarda los datos en una tabla de usuarios
    # Retorna un mensaje de éxito y un código de estado 201
    return {"message": "Usuario creado correctamente"}

def update_user(user_id: int, new_data: dict):
    # Lógica para actualizar los datos de un usuario por ID en la base de datos
    # Retorna un mensaje de éxito y un código de estado 202
    return {"message": f"Usuario con ID {user_id} actualizado correctamente"}

def delete_user(db: Session, user_id: int) -> bool:
    user_to_delete = get_user(db=db, user_id=user_id)

    if user_to_delete is None:
        return False

    db.delete(user_to_delete)
    db.commit()

    return True
