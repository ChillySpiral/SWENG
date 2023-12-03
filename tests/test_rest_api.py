import pytest
from fastapi.testclient import TestClient
from src.endpoints.rest_api import app
from src.repository.crud import CRUD
from src.entity.user_dto import UserDTO
from src.entity.post_dto import PostDTO

client = TestClient(app)
dba_default = CRUD()


def test_create_user():
    response = client.post(
        "/user/",
        json={"username": "user2", "password": "asdf"},
    )
    assert response.status_code == 200
