from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PostDTO(BaseModel):
    post_id: UUID
    user_id: UUID
    text: str
    image: str = ""
    image_small: str = ""
    sentiment_label: str = ""
    sentiment_score: str = ""
    posted: datetime
