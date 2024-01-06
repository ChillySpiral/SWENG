from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from uuid import UUID
from datetime import datetime

from src.model.comment_model import CommentResponse, CommentCreateModel
from src.model.user_model import UserModel, UserUpdateModel, UserBioModel, UserResponse, UserLoginResponse
from src.model.post_model import PostModel, PostCreateModel, PostResponse
from src.repository.crud import CRUD

app = FastAPI()
db_access = CRUD()


class RestAPI:

    def __init__(self):
        app.openapi = RestAPI.generate_openapi_contract()

    @staticmethod
    @app.get("/user/{user_id}", tags=["Users"])
    async def get_user(user_id: UUID) -> UserResponse:
        return db_access.get_user(user_id)

    @staticmethod
    @app.post("/user", tags=["Users"])
    async def create_user(user: UserBioModel) -> UserResponse:
        return db_access.insert_user(user)

    @staticmethod
    @app.put("/user", tags=["Users"])
    async def update_user(user: UserUpdateModel) -> UserResponse:
        return db_access.update_user(user)

    @staticmethod
    @app.delete("/user/{user_id}", tags=["Users"])
    async def delete_user(user_id: UUID) -> bool:
        return db_access.delete_user(user_id)

    @staticmethod
    @app.get("/users", tags=["Users"])
    async def get_all_users() -> list[UserResponse]:
        return db_access.get_all_users()

    @staticmethod
    @app.post("/user/login", tags=["Users"])
    async def login_user(user: UserModel) -> UserLoginResponse:
        return db_access.login_user(user)

    @staticmethod
    @app.get("/post/{post_id}", tags=["Posts"])
    async def get_post(post_id: UUID) -> PostResponse:
        return db_access.get_post(post_id)

    @staticmethod
    @app.post("/post", tags=["Posts"])
    async def create_post(post: PostCreateModel) -> PostResponse:
        return await db_access.insert_post(post)

    @staticmethod
    @app.put("/post", tags=["Posts"])
    async def update_post(post: PostModel) -> PostResponse:
        return db_access.update_post(post)

    @staticmethod
    @app.delete("/post/{post_id}", tags=["Posts"])
    async def delete_post(post_id: UUID) -> bool:
        return db_access.delete_post(post_id)

    @staticmethod
    @app.get("/posts", tags=["Posts"])
    async def get_all_posts() -> list[PostResponse]:
        return db_access.get_all_posts()

    @staticmethod
    @app.get("/posts/user/{user_id}", tags=["Posts"])
    async def get_posts_by_user(user_id: UUID) -> list[PostResponse]:
        return db_access.get_posts_by_user(user_id)

    @staticmethod
    @app.get("/post/newest", tags=["Posts"])
    async def get_newest_post() -> PostResponse:
        data: list[PostResponse] = db_access.get_all_posts()
        idx_newest = 0
        dt_max = datetime(1900, 1, 1, 1, 0)
        for idx, post in enumerate(data):
            if post.posted > dt_max:
                dt_max = post.posted
                idx_newest = idx
        return data[idx_newest]

    @staticmethod
    @app.post("/comment", tags=["Comments"])
    async def create_comment(comment: CommentCreateModel) -> CommentResponse:
        return db_access.insert_comment(comment)

    @staticmethod
    @app.get("/comment/{post_id}", tags=["Comments"])
    async def get_comments_by_post(post_id: UUID) -> list[CommentResponse]:
        return db_access.get_comments_by_post(post_id)

    @staticmethod
    @app.get("/comment/{post_id}/generate", tags=["Comments"])
    async def get_comment_generated(post_id: UUID, comment: str) -> str:
        return await db_access.generate_comment(post_id, comment)

    @staticmethod
    def generate_openapi_contract():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="SWENG Social Media App",
            version="0.0.2",
            description="This is a OpenAPI Schema which manages users and posts",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
