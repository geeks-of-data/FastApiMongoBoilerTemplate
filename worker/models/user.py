from pydantic import BaseModel, EmailStr
from typing import Union


class User(BaseModel):
    username: str = "kaanozbudak"
    name: str = "kaan"
    surname: Union[str, None] = None
    age: int = 25
    email: EmailStr = "kaanozbudak@hotmail.com"
