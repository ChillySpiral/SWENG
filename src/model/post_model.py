from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PostModel(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str = ""


class PostCreateModel(BaseModel):
    user_id: UUID
    text: str
    image: str = None


class PostResponse(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str = None
    sentiment_label: str = None
    sentiment_score: str = None
    posted: datetime


class PostImage(BaseModel):
    post_id: UUID
    image: str
