import pytest

from src.entity.user import UserDTO
from src.entity.post import PostDTO
from src.repository.db_access import DBAccess


def test_create_get_post():
    test_id: int = 0
    post_dto = PostDTO(post_id=test_id, user_id=1, text="post0")
    dba_default = DBAccess()
    dba_default.create_post(post_dto)
    result = dba_default.get_post(test_id)

    assert result.post_id == test_id
    assert result.text == "post0"


def test_create_get_user():
    test_id: int = 0
    user_dto = UserDTO(user_id=test_id, username="user0")
    dba_default = DBAccess()
    dba_default.create_user(user_dto)
    result = dba_default.get_user(test_id)

    assert result.user_id == test_id
    assert result.username == "user0"


def test_create_get_all_posts():
    dba_default = DBAccess()
    dba_default.create_post(PostDTO(post_id=1, user_id=1, text="post1"))
    dba_default.create_post(PostDTO(post_id=2, user_id=1, text="post2"))
    dba_default.create_post(PostDTO(post_id=3, user_id=1, text="post3"))
    result = dba_default.get_all_posts()

    # 4 because the database wasn't cleared before adding the new elements
    assert len(result) == 4


def test_create_get_all_users():
    dba_default = DBAccess()
    dba_default.create_user(UserDTO(user_id=1, username="user1"))
    dba_default.create_user(UserDTO(user_id=2, username="user2"))
    dba_default.create_user(UserDTO(user_id=3, username="user3"))
    result = dba_default.get_all_users()

    # 4 because the database wasn't cleared before adding the new elements
    assert len(result) == 4
