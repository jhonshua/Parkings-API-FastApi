# middleware.py
from fastapi import Request, HTTPException
from sqlalchemy.orm import Session
from models.user_model import User
from config.db_config import SessionLocal  # Importa tu configuración de base de datos
import jwt
import os

CLAVE = os.getenv('CLAVE_TOKEN')  # Obtén la clave secreta del entorno

def get_user_data(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    return user

def authenticate_user(request: Request):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Unauthorized: Token missing")

    try:
        token_type, token = authorization_header.split(" ")
        print(token) 
        if token_type.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid token type")

        payload = jwt.decode(token, CLAVE, algorithms=["HS256"])
        email = payload.get("email")  # Obtén el correo electrónico del token (puedes ajustar esto según tu payload)
        db = SessionLocal()
        user = get_user_data(db, email)
        db.close()

        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized: User not found")

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Unauthorized: Token expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
