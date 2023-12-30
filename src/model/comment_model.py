from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class CommentModel(BaseModel):
    comment_id: UUID
    post_id: UUID
    user_id: UUID
    text: str


class CommentCreateModel(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str


class CommentResponse(BaseModel):
    comment_id: UUID
    post_id: UUID
    user_id: UUID
    text: str
    posted: datetime
