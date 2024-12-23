from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI as FastAPI, Request

from models.user import user_model
from models.rol  import rol_model
from models.employees import employee_model

from routes.user import user_routes
from routes.auth import auth_routes
from routes.rol import rol_routes
from routes.employees import employees_routes

from config.db_config import  engine
from dotenv import load_dotenv
import os

#Creamos las tablas en la base de datos (si no existen)
user_model.Base.metadata.create_all(bind=engine)
employee_model.Base.metadata.create_all(bind=engine)
rol_model.Base.metadata.create_all(bind=engine)

#Inicializamos la aplicación FastAPI
app = FastAPI()

load_dotenv() 

CORS_ORIGINS = os.getenv('CORS_ORIGINS')

#Lista de orígenes permitidos (ajústala según tus necesidades)
origins = [
   CORS_ORIGINS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener los templates genericos 
templates = Jinja2Templates(directory="templates")

#repuesta para rutas no declaradas
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse("generic_template/404.html", {"request": request})

#Incluimos las rutas relacionadas con los usuarios
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(rol_routes.router, prefix="/roles", tags=["roles"])
app.include_router(employees_routes.router, prefix="/employee", tags=["employee"])

#rutas pendientes por realizar 
#reposrtes
#gestion de pagos
#Gestión de Estacionamientos
#egresos
#ingresos
#gestion de plazas
#incidencias
#reportes
