import pytest

from src.entity.post import PostDTO
from src.entity.user import UserDTO
from src.repository.dbdict import DBAccess


def test_insert_get_post():
    test_id: int = 5
    dba_default = DBAccess()
    dba_default.insert_post(PostDTO(test_id))
    result = dba_default.get_post(test_id)

    assert result.user_id == test_id


def test_insert_get_user():
    test_id: int = 5
    dba_default = DBAccess()
    dba_default.insert_user(UserDTO(test_id))
    result = dba_default.get_user(test_id)

    assert result.user_id == test_id


def test_insert_get_all_posts():
    dba_default = DBAccess()
    dba_default.insert_post(PostDTO(0))
    dba_default.insert_post(PostDTO(1))
    dba_default.insert_post(PostDTO(2))
    result = dba_default.get_all_posts()

    # 4 because the database wasn't cleared before adding the new elements
    assert len(result) == 4


def test_insert_get_all_users():
    dba_default = DBAccess()
    dba_default.insert_user(UserDTO(0))
    dba_default.insert_user(UserDTO(1))
    dba_default.insert_user(UserDTO(2))
    result = dba_default.get_all_users()
    print(result)

    # 4 because the database wasn't cleared before adding the new elements
    assert len(result) == 4