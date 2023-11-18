import json
from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    user_id: int = Field()
    Username: str = ""
    Password: str = ""

    def as_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
