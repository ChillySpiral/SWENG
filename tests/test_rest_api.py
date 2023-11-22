import pytest
import json
from fastapi.testclient import TestClient
from src.endpoints.rest_api import app
from src.repository.db_access import DBAccess
from src.entity.user import UserDTO
from src.entity.post import PostDTO

client = TestClient(app)
dba_default = DBAccess()


def pytest_sessionstart(session):
    dba_default.create_post(PostDTO(post_id=1, user_id=1, text="post1"))
    dba_default.create_user(UserDTO(user_id=1, Usernane="user1"))


def test_get_post():
    response = client.get("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"post_id": 1, "user_id": 1, "text": "post1", "image": ""}


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "password": "", "username": "user1"}


def test_create_post():
    response = client.post(
        "/posts/create/",
        json={"post_id": 2, "user_id": 1, "text": "test create post", "image": ""},
    )
    assert response.status_code == 200


def test_create_user():
    response = client.post(
        "/users/create/",
        json={"user_id": 2, "username": "user2", "password": "asdf"},
    )
    assert response.status_code == 200


def test_get_all_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert len(response.json()) == 4


