# Importamos la clase FastAPI
from fastapi import FastAPI

# Importamos el modelo de usuario
from models import user_model

# Importamos las rutas relacionadas con los usuarios
from routes import user_routes

# Importamos la configuración de la base de datos
from config.db_config import SessionLocal, engine

# Creamos las tablas en la base de datos (si no existen)
user_model.Base.metadata.create_all(bind=engine)

# Mensaje por consola para indicar que la conexión fue exitosa
print("Conexión a la base de datos exitosa")

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Definimos una dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Incluimos las rutas relacionadas con los usuarios
app.include_router(user_routes.router, prefix="/users", tags=["users"])

# Ejecutamos la aplicación si este archivo se ejecuta directamente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
