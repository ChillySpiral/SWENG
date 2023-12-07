import pytest
from src.entity.user_dto import UserDTO
from src.entity.post_dto import PostDTO
from src.entity.entities import Base, User, Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import UUID
from datetime import datetime


def test_user_dto():
    user_data = {"user_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "username": "john_doe", "password": "secret", "bio": "Hello, I'm John."}
    user_dto = UserDTO(**user_data)
    assert user_dto.user_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert user_dto.username == "john_doe"
    assert user_dto.password == "secret"
    assert user_dto.bio == "Hello, I'm John."


def test_post_dto():
    post_data = {"post_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "user_id": UUID("123e4567-e89b-12d3-a456-426614174002"),
                 "text": "This is a post", "image": "somebase64", "posted": datetime(2023, 1, 1, 12, 0, 0)}
    post_dto = PostDTO(**post_data)
    assert post_dto.post_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert post_dto.user_id == UUID("123e4567-e89b-12d3-a456-426614174002")
    assert post_dto.text == "This is a post"
    assert post_dto.image == "somebase64"
    assert post_dto.posted == datetime(2023, 1, 1, 12, 0, 0)


@pytest.fixture
def database():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_user_model(database):
    user_data = {"username": "john_doe", "password": "secret", "bio": "Hello, I'm John."}
    user = User(**user_data)

    database.add(user)
    database.commit()

    assert user.user_id is not None
    assert user.username == "john_doe"
    assert user.password == "secret"
    assert user.bio == "Hello, I'm John."
    assert user.posts == []


def test_post_model(database):
    user_data = {"username": "john_doe", "password": "secret", "bio": "Hello, I'm John."}
    user = User(**user_data)
    database.add(user)
    database.commit()

    post_data = {"user_id": user.user_id, "text": "This is a post", "image": "post_image.jpg",
                 "posted": datetime.utcnow()}
    post = Post(**post_data)

    user.posts.append(post)
    database.commit()

    assert post.post_id is not None
    assert post.user_id == user.user_id
    assert post.text == "This is a post"
    assert post.image == "post_image.jpg"
    assert post.posted is not None
    assert post.user == user
