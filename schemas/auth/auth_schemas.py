from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar


T = TypeVar('T')

class ResponseAuth(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    token: Optional[T] = None  
    


class AuthSchema(BaseModel):
    email: str
    password: str
  
    
class RequestAuth(BaseModel):
    parameter: AuthSchema = Field(...)