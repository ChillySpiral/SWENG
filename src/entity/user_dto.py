from uuid import UUID
from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: UUID
    username: str
    password: str
    bio: str | None = None
