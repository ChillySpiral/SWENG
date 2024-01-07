import json
import os
import uuid as uxid
from uuid import UUID
from datetime import datetime
import socket
from dotenv import load_dotenv

from src.repository.db_repository import Repository
from src.model.post_model import PostResponse, PostModel, PostCreateModel
from src.model.user_model import UserModel, UserResponse, UserLoginResponse, UserUpdateModel, UserBioModel
from src.model.comment_model import CommentResponse, CommentModel, CommentCreateModel

import aiokafka
from transformers import pipeline

# Set up and initialize database here
db = Repository()
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
load_dotenv("../.env")
KAFKA_RESPONSE_TOPIC_SA = os.getenv('KAFKA_SENTIMENT_ANALYSIS_RESPONSE')
KAFKA_REQUEST_TOPIC_SA = os.getenv('KAFKA_SENTIMENT_ANALYSIS_REQUEST')
KAFKA_RESPONSE_TOPIC_TG = os.getenv('KAFKA_TEXT_GENERATION_RESPONSE')
KAFKA_REQUEST_TOPIC_TG = os.getenv('KAFKA_TEXT_GENERATION_REQUEST')
KAFKA_REQUEST_TOPIC_RS = os.getenv('KAFKA_RESIZE_REQUEST')
KAFKA_RESPONSE_TOPIC_RS = os.getenv('KAFKA_RESIZE_RESPONSE')
KAFKA_HOST = os.getenv('KAFKA_HOST') + ":9092"


# ToDo: retain function names, but replace implementation with code that queries and filters an actual database
class CRUD:

    def __init__(self):
        self.__sa__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_RESPONSE_TOPIC_SA,
            group_id='text-generation_consumer',
            bootstrap_servers=KAFKA_HOST,
        )
        self.__tg__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_RESPONSE_TOPIC_TG,
            group_id='sentiment-analysis_consumer',
            bootstrap_servers=KAFKA_HOST
        )
        self.__rs__consumer__ = aiokafka.AIOKafkaConsumer(
            KAFKA_RESPONSE_TOPIC_RS,
            group_id='resize_consumer',
            bootstrap_servers='kafka:9092'
        )
        self.__producer__ = aiokafka.AIOKafkaProducer(
            bootstrap_servers=KAFKA_HOST, client_id=socket.gethostname())

        self.init_sa = 0
        self.init_tg = 0
        self.init_rs = 0

    @staticmethod
    def insert_user(user: UserBioModel) -> UserResponse:
        data = db.insert_user(user.username, user.password, user.bio)
        return UserResponse(user_id=data.user_id, username=data.username, bio=data.bio)

    @staticmethod
    def update_user(user: UserUpdateModel) -> UserResponse:
        data = db.update_user(user.user_id, user.username, user.password, user.bio)
        return UserResponse(user_id=data.user_id, username=data.username, bio=data.bio)

    @staticmethod
    def delete_user(user_id: UUID) -> bool:
        return db.delete_user(user_id)

    @staticmethod
    def get_user(user_id: UUID) -> UserResponse:
        data = db.get_user(user_id)
        return UserResponse(user_id=data.user_id, username=data.username, bio=data.bio)

    @staticmethod
    def get_all_users() -> list[UserResponse]:
        data = db.get_all_users()
        list_out: list[UserResponse] = []
        for user in data:
            list_out.append(UserResponse(user_id=user.user_id, username=user.username, bio=user.bio))
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
    def update_post(post: PostModel) -> PostResponse:
        data = db.update_post(post.post_id, post.text, post.image)
        return PostResponse(
            post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image, sentiment_label=data.sentiment_label, sentiment_score=data.sentiment_score, posted=data.posted)

    @staticmethod
    def delete_post(post_id: UUID) -> bool:
        return db.delete_post(post_id)

    @staticmethod
    def get_post(post_id: UUID) -> PostResponse:
        data = db.get_post(post_id)
        return PostResponse(
            post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image, sentiment_label=data.sentiment_label, sentiment_score=data.sentiment_score, posted=data.posted)

    @staticmethod
    def get_all_posts() -> list[PostResponse]:
        data = db.get_all_posts()
        list_out: list[PostResponse] = []
        for post in data:
            list_out.append(PostResponse(
                post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted))
        return list_out

    @staticmethod
    def get_posts_by_user(user_id: UUID) -> list[PostResponse]:
        data = db.get_posts_by_user(user_id)
        list_out: list[PostResponse] = []
        for post in data:
            list_out.append(PostResponse(
                post_id=post.post_id, user_id=post.user_id, text=post.text, image=post.image_small, sentiment_label=post.sentiment_label, sentiment_score=post.sentiment_score, posted=post.posted))
        return list_out

    @staticmethod
    def insert_comment(comment: CommentCreateModel) -> CommentResponse:
        data = db.insert_comment_to_post(comment.post_id, comment.user_id, comment.text, datetime.now())
        return CommentResponse(
            comment_id=data.comment_id, post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image,
            posted=data.posted)

    @staticmethod
    def get_comments_by_post(post_id: UUID) -> list[CommentResponse]:
        data = db.get_comments_by_post(post_id)
        list_out: list[CommentResponse] = []
        for comment in data:
            list_out.append(CommentResponse(
                comment_id=comment.comment_id, post_id=comment.post_id, user_id=comment.user_id, text=comment.text,
                posted=comment.posted))
        return list_out

    async def generate_comment(self, post_id: UUID, comment: str):
        await self.__producer__.start()
        if self.init_tg == 0:
            await self.__tg__consumer__.start()
            self.init_tg = 1

        byte_value = json.dumps(comment).encode("utf-8")
        byte_key = str(post_id).encode("utf-8")

        try:
            print(f"Sending Current Comment: " + comment + " in bytes: " + str(byte_value))
            print(f"Key: " + str(post_id) + " in bytes:" + str(byte_key))
            await self.__producer__.send(topic=KAFKA_REQUEST_TOPIC_TG, key=byte_key, value=byte_value)
            print(f"Awaiting response")
            async for msg in self.__tg__consumer__:
                text = msg.value.decode('utf-8')
                uuid = msg.key.decode('utf-8')
                print(f"Got sentiment for ID: " + str(uuid) + " message: " + str(text))
                if UUID(uuid) == post_id:
                    djs = json.loads(text)
                    return djs[0]['generated_text']
        except Exception as e:
            print(f"Error sending message: {e}")
        return ""

    async def insert_post(self, post: PostCreateModel) -> PostResponse:
        data = db.insert_post(post.user_id, post.text, post.image, datetime.now())
        await self.__producer__.start()
        if data.image:
            if self.init_rs == 0:
                await self.__rs__consumer__.start()
                self.init_rs = 1
            try:
                print(f"Post ID: " + str(data.post_id))
                byte_value = json.dumps(data.image).encode("utf-8")
                byte_key = str(data.post_id).encode("utf-8")
                await self.__producer__.send(topic=KAFKA_REQUEST_TOPIC_SA, key=byte_key, value=byte_value)
                print(f"Waiting for message to consume")
                async for msg in self.__rs__consumer__:
                    image = msg.value.decode('utf-8')
                    uuid = msg.key.decode('utf-8')
                    print(f"Got sentiment for ID: " + str(uuid) + " message: " + str(image))
                    if UUID(uuid) == data.post_id:
                        #ToDO
                        break
            except Exception as e:
                print(f"Error sending message: {e}")

        elif data.text:
            if self.init_sa == 0:
                await self.__sa__consumer__.start()
                self.init_sa = 1
            try:
                print(f"Post ID: " + str(data.post_id))
                byte_value = json.dumps(data.text).encode("utf-8")
                byte_key = str(data.post_id).encode("utf-8")
                await self.__producer__.send(topic=KAFKA_REQUEST_TOPIC_SA, key=byte_key, value=byte_value)
                print(f"Waiting for message to consume")
                async for msg in self.__sa__consumer__:
                    text = msg.value.decode('utf-8')
                    uuid = msg.key.decode('utf-8')
                    print(f"Got sentiment for ID: " + str(uuid) + " message: " + str(text))
                    if UUID(uuid) == data.post_id:
                        djs = json.loads(text)
                        data = db.update_post_sentiment(data.post_id, djs["label"], str(djs["score"]))
                        break
            except Exception as e:
                print(f"Error sending message: {e}")

        return PostResponse(post_id=data.post_id, user_id=data.user_id, text=data.text, image=data.image_small, sentiment_label=data.sentiment_label, sentiment_score=data.sentiment_score, posted=data.posted)


