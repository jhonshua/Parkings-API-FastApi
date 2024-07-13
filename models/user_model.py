# Importamos las clases necesarias de SQLAlchemy
from sqlalchemy import Boolean, Column, Integer, String

# Importamos la clase base declarativa que definimos previamente en db_config.py
from config.db_config import Base

# Definimos la clase de modelo para los usuarios
class User(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "users"

    # Columna para el ID (clave primaria)
    id = Column(Integer, primary_key=True)

    # Columna para el correo electrónico (único e indexado)
    email = Column(String, unique=True, index=True)

    # Columna para almacenar la contraseña hasheada
    password = Column(String)

    # Columna para indicar si el usuario está activo (por defecto, True)
    is_active = Column(Boolean, default=True)

  


