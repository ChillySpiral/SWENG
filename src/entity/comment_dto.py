from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class CommentDTO(BaseModel):
    comment_id: UUID
    post_id: UUID
    user_id: UUID
    text: str
    image: str = ""
    posted: datetime