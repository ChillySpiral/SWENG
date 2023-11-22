from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.entity.post import PostDTO
from src.entity.user import UserDTO
from src.repository.db_access import DBAccess

app = FastAPI()
db_access = DBAccess()


class RestAPI:
    def __init__(self):
        app.openapi = RestAPI.generate_openapi_contract()

    @staticmethod
    @app.post("/posts/create/", tags=["Create", "Posts"])
    async def create_post(post: PostDTO):
        db_access.create_post(post)

    @staticmethod
    @app.get("/posts/{post_id}", tags=["Get", "Posts"])
    async def get_post(post_id: int) -> PostDTO:
        return db_access.get_post(post_id)

    @staticmethod
    @app.get("/posts/{user_id}", tags=["Get", "Posts"])
    async def get_post_by_user(user_id: int) -> list[PostDTO]:
        return db_access.get_posts_by_user(user_id)

    @staticmethod
    @app.get("/posts/", tags=["Get", "Posts"])
    async def get_all_posts() -> list[PostDTO]:
        return db_access.get_all_posts()

    @staticmethod
    @app.post("/users/create/", tags=["Create", "Users"])
    async def create_user(user: UserDTO):
        db_access.create_user(user)

    @staticmethod
    @app.get("/users/{user_id}", tags=["Get", "Users"])
    async def get_post(user_id: int) -> UserDTO:
        return db_access.get_user(user_id)

    @staticmethod
    def generate_openapi_contract():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="SWENG Social Media",
            version="0.0.1",
            description="This is a OpenAPI Schema which manages users and posts in a dictionary",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema



