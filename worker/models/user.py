from pydantic import BaseModel, EmailStr
from typing import Union


class User(BaseModel):
    username: str
    name: str = "kaan"
    surname: Union[str, None] = "surname"
    age: int = 25
    email: EmailStr = "kaanozbudak@hotmail.com"
