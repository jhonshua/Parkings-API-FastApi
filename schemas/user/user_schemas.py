from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar


T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None  
    
    
class Ability(BaseModel):
    read: bool
    write: bool
    edit: bool
    delete: bool

class UserSchema(BaseModel):
    full_name: str
    username: str
    email: str
    password: str
    phone: int
    status:str
    rol_id:str
    ability: Ability  
    
class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)