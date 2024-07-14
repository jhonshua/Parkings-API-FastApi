from fastapi import FastAPI
from models import user_model
from routes import user_routes
from config.db_config import  engine

# Creamos las tablas en la base de datos (si no existen)
user_model.Base.metadata.create_all(bind=engine)

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Incluimos las rutas relacionadas con los usuarios
app.include_router(user_routes.router, prefix="/users", tags=["users"])


