import pytest
from src.model.user_model import UserModel, UserBioModel, UserResponse, UserUpdateModel, UserLoginResponse
from src.model.post_model import PostModel, PostCreateModel, PostResponse
from uuid import UUID
from datetime import datetime


def test_user_model():
    user_data = {"username": "john_doe", "password": "secret"}
    user = UserModel(**user_data)
    assert user.username == "john_doe"
    assert user.password == "secret"


def test_user_bio_model():
    user_data = {"username": "john_doe", "password": "secret", "bio": "Hello, I'm John."}
    user_bio = UserBioModel(**user_data)
    assert user_bio.username == "john_doe"
    assert user_bio.password == "secret"
    assert user_bio.bio == "Hello, I'm John."


def test_user_response():
    user_data = {"user_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "username": "john_doe", "bio": "Hello, I'm John."}
    user_response = UserResponse(**user_data)
    assert user_response.user_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert user_response.username == "john_doe"
    assert user_response.bio == "Hello, I'm John."


def test_user_update_model():
    update_data = {"user_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "username": "john_doe", "password": "new_secret", "bio": "Updated bio."}
    user_update = UserUpdateModel(**update_data)
    assert user_update.user_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert user_update.username == "john_doe"
    assert user_update.password == "new_secret"
    assert user_update.bio == "Updated bio."


def test_user_login_response():
    login_response_data = {"success": True, "user_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "username": "john_doe"}
    login_response = UserLoginResponse(**login_response_data)
    assert login_response.success is True
    assert login_response.user_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert login_response.username == "john_doe"


def test_post_model():
    post_data = {"post_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "user_id": UUID("123e4567-e89b-12d3-a456-426614174002"),
                 "text": "This is a post", "image": "somebase64"}
    post = PostModel(**post_data)
    assert post.post_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert post.user_id == UUID("123e4567-e89b-12d3-a456-426614174002")
    assert post.text == "This is a post"
    assert post.image == "somebase64"


def test_post_create_model():
    post_create_data = {"user_id": UUID("123e4567-e89b-12d3-a456-426614174002"), "text": "New post", "image": "somebase64"}
    post_create = PostCreateModel(**post_create_data)
    assert post_create.user_id == UUID("123e4567-e89b-12d3-a456-426614174002")
    assert post_create.text == "New post"
    assert post_create.image == "somebase64"


def test_post_response():
    post_response_data = {"post_id": UUID("123e4567-e89b-12d3-a456-426614174001"), "user_id": UUID("123e4567-e89b-12d3-a456-426614174002"),
                          "text": "This is a post", "image": "somebase64", "posted": datetime(2023, 1, 1, 12, 0, 0)}
    post_response = PostResponse(**post_response_data)
    assert post_response.post_id == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert post_response.user_id == UUID("123e4567-e89b-12d3-a456-426614174002")
    assert post_response.text == "This is a post"
    assert post_response.image == "somebase64"
    assert post_response.posted == datetime(2023, 1, 1, 12, 0, 0)
