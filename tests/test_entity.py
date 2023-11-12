import pytest

from src.entity.user import UserDTO


@pytest.fixture()
def user_dto_default():
    return UserDTO(0)


@pytest.fixture()
def post_dto_default():
    return UserDTO(0)


def test_UserDTO_set_id():
    test_id: int = 1
    user_dto_default.Id = test_id

    assert user_dto_default.Id == test_id


def test_UserDTO_set_username():
    test_string: str = "test"
    user_dto_default.Username = test_string

    assert user_dto_default.Username == test_string


def test_UserDTO_set_password():
    test_string: str = "test"
    user_dto_default.Password = test_string

    assert user_dto_default.Password == test_string


def test_PostDTO_set_id():
    test_id: int = 1
    post_dto_default.Id = test_id

    assert post_dto_default.Id == test_id


def test_PostDTO_set_user_id():
    test_id: int = 1
    post_dto_default.user_id = test_id

    assert post_dto_default.user_id == test_id


def test_PostDTO_set_text():
    test_string: str = "test"
    post_dto_default.text = test_string

    assert post_dto_default.text == test_string


def test_PostDTO_set_image():
    test_string: str = "test"
    post_dto_default.image = test_string

    assert post_dto_default.image == test_string