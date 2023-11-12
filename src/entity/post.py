from sqliteframe import Database, table, String, Integer, Boolean, ForeignKey, Blob
from pathlib import Path

from src.entity.user import User

database = Database(Path("../../sweng.db"), output=True)


class Post_DTO:
    def __init__(self):
        self.Id = None
        self.user_id = None
        self.text = ""
        self.image = ""


@table(database)
class Post:
    Id = Integer(primary_key=True)
    user_id = ForeignKey(User)
    text = String(nullable=True)
    image = Blob(nullable=True)
