from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import user_model
from routes.user import user_routes
from routes.auth import auth_routes
from config.db_config import  engine

# Creamos las tablas en la base de datos (si no existen)
user_model.Base.metadata.create_all(bind=engine)

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Lista de orígenes permitidos (ajústala según tus necesidades)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluimos las rutas relacionadas con los usuarios
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])

