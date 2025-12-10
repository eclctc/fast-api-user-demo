from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    gender: str
    country: str
    isActive: bool


# UserCreate extends UserBase by adding a password field for user creation.
class UserCreate(UserBase):
    password: str

# User also extends UserBase but includes an id, representing a stored user.
class User(UserBase):
    id: int
    # Config class makes it compatible with SQLAlchemy ORM.
    class Config:
        orm_mode = True