import os
from datetime import datetime
from uuid import UUID

from dotenv import load_dotenv
from sqlalchemy import URL, select, and_
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.entity.entities import Base, Post, Comment
from src.entity.entities import User
from src.entity.post_dto import PostDTO
from src.entity.user_dto import UserDTO
from src.entity.comment_dto import CommentDTO


class UserNotFoundException:
    pass


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
            host=os.getenv("DB_HOST"),
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
            user_dto_list = list(map(lambda user: UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio), user_list))
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
            return UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio)

    def delete_user(self, user_id: UUID) -> bool:
        with Session(self.engine) as session:
            statement = select(User).where(User.user_id == user_id)
            user = session.scalar(statement)
            if user is None:
                return False
            session.delete(user)
            session.commit()
            return True

    def get_user_login(self, username:str, password:str) -> UserDTO:
        with Session(self.engine) as session:
            statement = select(User).where(and_(User.username == username, User.password == password))
            user = session.scalar(statement)
            if user is None:
                raise UserNotFoundException("No user found with the provided username.")
            return UserDTO(user_id=user.user_id, username=user.username, password=user.password, bio=user.bio)

    def insert_post(self, user_id: UUID, text: str, image: str, posted: datetime, sentiment_label: str = "", sentiment_score: str = "", ) -> PostDTO:
        with Session(self.engine) as session:
            post = Post(user_id=user_id, text=text, image=image, image_small="", sentiment_label=sentiment_label, sentiment_score=sentiment_score, posted=posted)
            session.add(post)
            session.commit()
            return PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, posted=post.posted)

    def update_post(self, post_id: UUID, text: str, image: str) -> PostDTO:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            post.post_id = post_id
            post.text = text
            post.image = image
            session.commit()
            return PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, image_small=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted)

    def update_post_sentiment(self, post_id: UUID, sentiment_label: str, sentiment_score: str) -> PostDTO:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            post.post_id = post_id
            post.sentiment_label = sentiment_label
            post.sentiment_score = sentiment_score
            session.commit()
            return PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, image_small=post.image_small, sentiment_score=sentiment_score, sentiment_label=sentiment_label, posted=post.posted)

    def delete_post(self, post_id: UUID) -> bool:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            if post is None:
                return False
            session.delete(post)
            session.commit()
            return True

    def get_post(self, post_id: UUID) -> PostDTO:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            return PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, image_small=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted)

    def get_all_posts(self) -> list[PostDTO]:
        with Session(self.engine) as session:
            statement = select(Post)
            post_list = session.scalars(statement).all()
            post_dto_list = list(map(lambda post: PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, image_small=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted), post_list))
            return post_dto_list

    def get_posts_by_user(self, user_id: UUID) -> list[PostDTO]:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.user_id == user_id)
            post_list = session.scalars(statement).all()
            post_dto_list = list(map(lambda post: PostDTO(post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, image_small=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted), post_list))
            return post_dto_list

    def insert_comment_to_post(self,post_id: UUID, user_id: UUID, text: str, posted: datetime) -> CommentDTO:
        with Session(self.engine) as session:
            comment = Comment(post_id=post_id, user_id=user_id, text=text, posted=posted)
            session.add(comment)
            session.commit()
            return CommentDTO(comment_id=comment.comment_id, post_id=comment.post_id, user_id=comment.user_id, text=comment.text, posted=comment.posted)

    def get_comments_by_post(self, post_id: UUID) -> list[CommentDTO]:
        with Session(self.engine) as session:
            statement = select(Comment).where(Comment.post_id == post_id)
            comment_list = session.scalars(statement).all()
            comment_dto_list = list(map(lambda comment: CommentDTO(comment_id=comment.comment_id, post_id=comment.post_id, user_id=comment.user_id, text=comment.text, posted=comment.posted), comment_list))
            return comment_dto_list

    def internal_get_image_by_post(self, post_id: UUID) -> str:
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            return post.image

    def internal_save_small_image_by_post(self, post_id: UUID, small_image: str):
        with Session(self.engine) as session:
            statement = select(Post).where(Post.post_id == post_id)
            post = session.scalar(statement)
            post.post_id = post_id
            post.image_small = small_image
            session.commit()
