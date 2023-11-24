from uuid import UUID
from datetime import datetime
from src.repository.db_temp import DBTemp
from src.model.post_model import PostResponse, PostModel, PostCreateModel
from src.model.user_model import UserModel, UserResponse, UserLoginResponse, UserUpdateModel

# Set up and initialize database here
db = DBTemp()


# ToDo: retain function names, but replace implementation with code that queries and filters an actual database
class CRUD:

    @staticmethod
    def insert_user(user: UserModel) -> UserResponse:
        data = db.insert_user(user.username, user.password)
        return UserResponse(user_id=data.user_id, username=data.username)

    @staticmethod
    def update_user(user: UserUpdateModel) -> UserResponse:
        data = db.update_user(user.user_id, user.username, user.password)
        return UserResponse(user_id=data.user_id, username=data.username)

    @staticmethod
    def delete_user(user_id: UUID) -> bool:
        return db.delete_user(user_id)

    @staticmethod
    def get_user(user_id: UUID) -> UserResponse:
        data = db.get_user(user_id)
        return UserResponse(user_id=data.user_id, username=data.username)

    @staticmethod
    def get_all_users() -> list[UserResponse]:
        data = db.get_all_users()
        list_out: list[UserResponse] = []
        for user in data:
            list_out.append(UserResponse(user_id=user.user_id, username=user.username))
        return list_out

    # ToDo: maybe refactor to separate layer responsible for handling login (but it's a 2 ECTS course...)
    @staticmethod
    def login_user(user: UserModel) -> UserLoginResponse:
        data = db.get_user_login(user.username, user.password)
        success = False
        if data.user_id != UUID('00000000000000000000000000000000'):
            success = True
        return UserLoginResponse(success=success, user_id=data.user_id, username=data.username)

    @staticmethod
    def insert_post(post: PostCreateModel) -> PostResponse:
        data = db.insert_post(post.user_id, post.text, post.image, datetime.now())
        return PostResponse(
            post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image, posted=data.posted)

    @staticmethod
    def update_post(post: PostModel) -> PostResponse:
        data = db.update_post(post.post_id, post.text, post.image)
        return PostResponse(
            post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image, posted=data.posted)

    @staticmethod
    def delete_post(post_id: UUID) -> bool:
        return db.delete_post(post_id)

    @staticmethod
    def get_post(post_id: UUID) -> PostResponse:
        data = db.get_post(post_id)
        return PostResponse(
            post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image, posted=data.posted)

    @staticmethod
    def get_all_posts() -> list[PostResponse]:
        data = db.get_all_posts()
        list_out: list[PostResponse] = []
        for post in data:
            list_out.append(PostResponse(
                post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, posted=post.posted))
        return list_out

    @staticmethod
    def get_posts_by_user(user_id: UUID) -> list[PostResponse]:
        data = db.get_posts_by_user(user_id)
        list_out: list[PostResponse] = []
        for post in data:
            list_out.append(PostResponse(
                post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image, posted=post.posted))
        return list_out