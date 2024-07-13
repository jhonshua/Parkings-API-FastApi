# Importamos las funciones necesarias de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos la cadena de conexión a la base de datos (SQLite en este caso)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# También puedes usar PostgreSQL descomentando la siguiente línea y proporcionando la cadena de conexión adecuada
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Creamos una instancia del motor de base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Creamos una sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definimos una clase base declarativa para nuestros modelos
Base = declarative_base()
