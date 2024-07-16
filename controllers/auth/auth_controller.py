from sqlalchemy.orm import Session
from models.user_model import User
from config.db_config import SessionLocal
from schemas.auth.auth_schemas import AuthSchema
from passlib.context import CryptContext
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
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_data(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    return user 

def login(user_data: AuthSchema, db: Session) -> bool|str:
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
def logout() :
    return print('hola mundo')

#reset pass

def reset() :
    return print('hola mundo')