from sqlalchemy.orm import Session
from models.user.user_model import User
from schemas.user.user_schemas import UserSchema
from utils.helper_functions import get_password_hash
import json

#todos los usarios
def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

#un usuario por id
def get_user(db: Session, user_id: int):
     return db.query(User).filter(User.id == user_id).first()
 
#creamos usuario
def create_user(db: Session, user_data: UserSchema):
    
     full_name=user_data['full_name']
     full_name_json = json.dumps(full_name)
     username=user_data['username']
     username_json = json.dumps(username)
     email=user_data['email']
     email_json = json.dumps(email)
     password=user_data['password']
     password_hash = get_password_hash(password)
     phone=user_data['phone']
     phone_json = json.dumps(phone)
     status=user_data['status']
     status_json = json.dumps(status)
     rol_id=user_data['rol_id']
     rol_id_json = json.dumps(rol_id)
     ability=user_data['ability']
     ability_json = json.dumps(ability)
     
     _User = User(
        full_name=full_name_json.strip('"'),
        username=username_json.strip('"'),
        email=email_json.strip('"'),
        password= password_hash,
        phone=phone_json.strip('"'),
        status=status_json.strip('"'),
        rol_id=rol_id_json.strip('"'),
        ability=ability_json.strip('"')
    )
     db.add(_User)
     db.commit()
     db.refresh(_User)
     return _User
 
 
#actualizamos usuario 
def update_user(db: Session, user_id: int, user_data: UserSchema):
    user = get_user(db=db, user_id=user_id)
   
    full_name=user_data['full_name']
    full_name_json = json.dumps(full_name)
    username=user_data['username']
    username_json = json.dumps(username)
    email=user_data['email']
    email_json = json.dumps(email)
    password=user_data['password']
    password_json = json.dumps(password)
    phone=user_data['phone']
    phone_json = json.dumps(phone)
    status=user_data['status']
    status_json = json.dumps(status)
    rol_id=user_data['rol_id']
    rol_id_json = json.dumps(rol_id)
    ability=user_data['ability']
    ability_json = json.dumps(ability)
     
    user.full_name=full_name_json,
    user.username=username_json,
    user.email=email_json,
    user.password=password_json,
    user.phone=phone_json,
    user.status=status_json,
    user.rol_id=rol_id_json,
    user.ability=ability_json
   
    db.commit()
    db.refresh(user)
    return user
   
   
def delete_user(db: Session, user_id: int) -> bool:
    user_to_delete = get_user(db=db, user_id=user_id)
    if user_to_delete is None:
        return False
    db.delete(user_to_delete)
    db.commit()

    return True