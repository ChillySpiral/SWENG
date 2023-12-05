import os

from dotenv import load_dotenv
from sqlalchemy import URL, select
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from uuid import UUID
from src.entity.entities import Base
from src.entity.entities import User
from src.entity.user_dto import UserDTO


class Repository:
    _instance = None
    engine = None
    session = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Repository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        load_dotenv()
        database_url_object = URL.create(
            "postgresql",
            username=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host="localhost",
            port=5432,
            database=os.getenv("DB_NAME"),
        )
        self.engine = create_engine(database_url_object)
        Base.metadata.create_all(self.engine)  # Create all tables
        print(Base.metadata.tables)

    def insert_user(self, username: str, password: str, bio: str) -> UserDTO:
        with Session(self.engine) as session:
            user = User(username=username, password=password, bio=bio)
            session.add(user)
            session.commit()
            session.refresh(user)
        return UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio)

    def get_user(self, user_id: UUID) -> UserDTO:
        with Session(self.engine) as session:
            statement = select(User).where(User.user_id == user_id)
            user = session.scalar(statement)
        return UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio)

    def get_all_users(self) -> list[UserDTO]:
        with Session(self.engine) as session:
            statement = select(User)
            user_list = session.scalars(statement).all()
            user_dto_list = list(map(lambda user: UserDTO(user_id=user.user_id, username=user.username,
                                                          password=user.password, bio=user.bio), user_list))
        return user_dto_list

    def update_user(self, user_id: UUID, username: str, password: str, bio: str) -> UserDTO:
        with Session(self.engine) as session:
            statement = select(User).where(User.user_id == user_id)
            user = session.scalar(statement)
            user.user_id = user_id
            user.username = username
            user.password = password
            user.bio = bio
            session.commit()
            session.refresh(user)
        return UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio)

    def delete_user(self, user_id: UUID) -> bool:
        with Session(self.engine) as session:
            statement = select(User).where(User.user_id == user_id)
            user = session.scalar(statement)
            if user is None:
                return False
            session.delete(user)
            session.commit()
            session.flush()
            return True
