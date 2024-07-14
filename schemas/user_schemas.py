from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar


T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None  