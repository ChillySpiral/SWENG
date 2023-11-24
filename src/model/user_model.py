from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    user_id: UUID
    username: str


class UserUpdateModel(BaseModel):
    user_id: UUID
    username: str
    password: str


class UserLoginResponse(BaseModel):
    success: bool
    user_id: UUID
    username: str
