'''import pytest
from src.entity.user_dto import UserDTO
from src.entity.post_dto import PostDTO
from src.repository.crud import CRUD
from src.model.post_model import PostResponse, PostModel, PostCreateModel
from src.model.user_model import UserModel, UserResponse, UserLoginResponse, UserUpdateModel, UserBioModel


def test_create_user():
    username_test: str = "Test"
    password_test: str = "PwTest"
    bio_test: str = "I am some user"
    result: UserResponse = CRUD().insert_user(UserBioModel(
        username=username_test, password=password_test, bio=bio_test))

    assert result.username == username_test
    assert result.bio == bio_test'''