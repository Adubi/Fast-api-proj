from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID,uuid4
class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin ="admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class Userupdaterequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    
    

