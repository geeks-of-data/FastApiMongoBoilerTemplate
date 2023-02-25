from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    username: str
    name: str
    surname: Union[str, None] = None
    age: int
    email: str
