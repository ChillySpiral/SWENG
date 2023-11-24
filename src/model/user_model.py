from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class UserBioModel(BaseModel):
    username: str
    password: str
    bio: str = None


class UserResponse(BaseModel):
    user_id: UUID
    username: str
    bio: str = None


class UserUpdateModel(BaseModel):
    user_id: UUID
    username: str
    password: str
    bio: str = ""


class UserLoginResponse(BaseModel):
    success: bool
    user_id: UUID
    username: str
