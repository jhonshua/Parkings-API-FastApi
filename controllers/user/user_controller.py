from sqlalchemy.orm import Session
from models.user.user_model import User
from schemas.user.user_schemas import EmailSchema, UserSchema, New_userSchema
from utils.helper_functions import get_password_hash
from utils.send_mail import send_email
import json

#Todos los usuarios.
from sqlalchemy import or_

def get_all_users(db: Session, 
                  skip: int = 0, 
                  limit: int = 100, 
                  sort: str = "asc", 
                  full_name: str = None):

    query = db.query(User)

    # Si se proporciona un término de búsqueda, filtramos por nombre completo
    if full_name:
        query = query.filter(User.full_name.ilike(f"%{full_name}%"))

    # Ordenamos los resultados según el criterio especificado
    if sort:
        if sort == "asc":
            query = query.order_by(User.full_name.asc())
        elif sort == "desc":
            query.order_by(User.full_name.desc())

    # Aplicamos paginación
    return query.offset(skip).limit(limit).all()



#Un usuario por ID.
def get_user(db: Session, user_id: int):
     return db.query(User).filter(User.id == user_id).first()
 
#Creamos usuario.
def create_user(db: Session, user_data: UserSchema):
     
    _User = User(
        full_name = user_data.full_name,
        username = user_data.username,
        email = user_data.email,
        password = get_password_hash(user_data.password) ,
        phone=user_data.phone,
        statu=user_data.statu,
        rol_id=user_data.rol_id,
    )
    
    db.add(_User)
    db.commit()
    db.refresh(_User) 
    data=New_userSchema(template = "new_user",email = user_data.email, password = user_data.password, name = user_data.full_name)
    send_email(data)
    
    return _User
 
 
#Actualizamos usuario.
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
    statu=user_data['status']
    status_json = json.dumps(statu)
    rol_id=user_data['rol_id']
    rol_id_json = json.dumps(rol_id)

     
    user.full_name=full_name_json,
    user.username=username_json,
    user.email=email_json,
    user.password=password_json,
    user.phone=phone_json,
    user.status=status_json,
    user.rol_id=rol_id_json
   
    db.commit()
    db.refresh(user)
    
    
    
    return user
   
#Eliminamos usuario.
def delete_user(db: Session, user_id: int) -> bool:
    user_to_delete = get_user(db=db, user_id=user_id)
    if user_to_delete is None:
        return False
    db.delete(user_to_delete)
    db.commit()

    return True