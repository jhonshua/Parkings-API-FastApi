from sqlalchemy.orm import Session
from config.db_config import SessionLocal
from utils.helper_functions import verify_password, get_user_data
from utils.send_mail import send_email_password
from schemas.auth.auth_schemas import AuthSchema, InvalidTokenSchema,ResetPasswordRequest
from models.token.invalid_token import InvalidToken

from dotenv import load_dotenv
import os
import json
import datetime
import jwt

load_dotenv()  # Esto carga el archivo .env

CLAVE = os.getenv('CLAVE_TOKEN')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#login
def login(user_data: AuthSchema, db: Session) -> bool|str:
    #tengo que cambiar el diccionario que llega por un objeto
    email_to_search = json.dumps(user_data['email'])
    password_user = json.dumps(user_data['password']).strip('"')
    user = get_user_data(db, email_to_search.strip('"'))
    if user and verify_password(password_user, user.password):
        # Usuario existe y contraseña válida
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        payload = {
            "sub": user.id,  # ID del usuario (puedes usar otro identificador único)
            "email":user.email,
            "exp": expiration,
        }
        secret_key = CLAVE  # Cambia esto por una clave segura
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token  # Usuario existe y contraseña válida
    else:
        return False  # Usuario no existe o contraseña incorrecta
 
 
#logout
def logout(data: InvalidTokenSchema, db: Session)-> str:
    token = InvalidToken(
        user_id = data.user_id ,
        token = data.token
    ) 
    
    db.add(token)
    db.commit()
    db.refresh(token)
    token_response = ""
    return token_response

  
#reset pass
def reset(user_data: ResetPasswordRequest, db: Session) -> bool|str:
    print("me ejecuto")
    email = user_data.email
    user = get_user_data(db, email)
    if user :
        # tengo que generar un nuevo pass y enviarlo al correo
        # send_email_password(data = email)
        return True
    else:
        return False  # Usuario no existe o contraseña incorrecta
    