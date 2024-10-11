from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
