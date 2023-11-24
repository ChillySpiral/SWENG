from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PostModel(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str = None


class PostCreateModel(BaseModel):
    user_id: UUID
    text: str
    image: str = None


class PostResponse(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str = None
    posted: datetime
