import os

from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from entity.entities import Base
from src.repository.db_repository import Repository


def main():
    repository = Repository()
    user_dto = repository.insert_user(username="test", password="test", bio="hello there world")
    user_dto = repository.get_user(user_dto.user_id)
    user_dto = repository.update_user(user_id= user_dto.user_id, username="test", password="test", bio="hello there "
                                                                                                       "updated world")
    user_dto = repository.get_user(user_dto.user_id)
    repository.insert_user(username="user2", password="test", bio="hello there world")

    print(repository.get_all_users())
    repository.delete_user(user_dto.user_id)
    repository.delete_user(user_dto.user_id)


if __name__ == '__main__':
    main()
