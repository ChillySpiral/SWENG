from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PostDTO(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str | None = None
    posted: datetime
