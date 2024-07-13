from pydantic import BaseModel

# Definimos una clase base para los esquemas de usuario
class UserBase(BaseModel):
    email: str

# Definimos un esquema para la creación de usuarios (hereda de UserBase)
class UserCreate(UserBase):
    password: str

# Definimos un esquema completo para los usuarios (hereda de UserBase)
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
