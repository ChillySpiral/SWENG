from sqliteframe import Database, table, String, Integer, Boolean, ForeignKey
from pathlib import Path

database = Database(Path("sweng.db"), output=True)


class User_DTO:
    def __init__(self):
        self.Id = None
        self.Username = ""
        self.Password = ""


@table(database)
class User:
    id = Integer(primary_key=True)
    username = String(nullable=False)
    password = String(nullable=False)
