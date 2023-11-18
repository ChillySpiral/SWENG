from typing import Dict, Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.entity.post import PostDTO
from src.repository.dbdict import DBAccess

app = FastAPI()
db_access = DBAccess()


class RestAPI:

    @staticmethod
    @app.post("/create/posts/", tags=["Create", "Posts"])
    async def read_post(post: PostDTO):
        db_access.insert_post(post)

    @staticmethod
    @app.get("/read/posts/{post_id}", tags=["Read", "Posts"])
    async def read_post(post_id: int) -> PostDTO:
        return db_access.get_post(post_id)

    @staticmethod
    @app.get("/read/posts/", tags=["Read", "Posts"])
    async def read_posts() -> list[PostDTO]:
        return db_access.get_all_posts()

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


app.openapi = RestAPI.generate_openapi_contract()
