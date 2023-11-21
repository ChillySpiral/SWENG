import pytest
from fastapi.testclient import TestClient
from src.endpoints.rest_api import app
from src.repository.dbdict import DBAccess
from src.entity.user import UserDTO
from src.entity.post import PostDTO

client = TestClient(app)
dba_default = DBAccess()

# info: requires installation of httpx


def pytest_sessionstart(session):
    dba_default.insert_post(PostDTO(post_id=1, user_id=1, text="post1"))
    dba_default.insert_user(UserDTO(user_id=1, Usernane="user1"))


def test_get_post():
    response = client.get("/read/posts/1")
    assert response.status_code == 200
    assert response.json() == {"post_id": 1, "user_id": 1, "text": "post1", "image": ""}
