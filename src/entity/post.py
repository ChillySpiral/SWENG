import json
from pydantic import BaseModel, Field


class PostDTO(BaseModel):
    post_id: int = Field()
    user_id: int = Field()
    text: str = ""
    image: str = ""

    def to_dict(self):
        return self.__dict__

    def as_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def list_as_json(data):
        if isinstance(data, list):
            return json.dumps([obj.to_dict() for obj in data])
