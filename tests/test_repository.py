import pytest
from src.entity.user_dto import UserDTO
from src.entity.post_dto import PostDTO
from src.repository.crud import CRUD
from src.model.post_model import PostResponse, PostModel, PostCreateModel
from src.model.user_model import UserModel, UserResponse, UserLoginResponse, UserUpdateModel


def test_create_user():
    username_test: str = "Test"
    password_test: str = "PwTest"
    result: UserResponse = CRUD().insert_user(UserModel(username=username_test, password=password_test))

    assert result.username == username_test
