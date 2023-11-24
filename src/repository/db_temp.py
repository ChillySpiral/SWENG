import uuid
from uuid import UUID
from datetime import datetime
from src.entity.user_dto import UserDTO
from src.entity.post_dto import PostDTO


# Temporary database using typed lists to represent tables
class DBTemp:
    _instance = None
    table_users: list[UserDTO] = []
    table_posts: list[PostDTO] = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBTemp, cls).__new__(cls)
        return cls._instance

    def __int__(self):
        self.table_users = []
        self.table_posts = []

    def insert_user(self, username: str, password: str, bio: str) -> UserDTO:
        new = UserDTO(user_id=uuid.uuid4(), username=username, password=password, bio=bio)
        self.table_users.append(new)
        return UserDTO(user_id=new.user_id, username=new.username, password=new.password, bio=new.bio)

    def update_user(self, user_id: UUID, username: str, password: str, bio: str) -> UserDTO:
        user_updated: UserDTO = UserDTO(
            user_id=UUID('00000000000000000000000000000000'), username="error", password="error", bio="error")
        for user in self.table_users:
            if user.user_id == user_id:
                user.username = username
                user.password = password
                user.bio = bio
                user_updated = user
        return user_updated

    def delete_user(self, user_id: UUID) -> bool:
        success = False
        for user in self.table_users:
            if user.user_id == user_id:
                self.table_users.remove(user)
                success = True
        return success

    def get_user(self, user_id: UUID) -> UserDTO:
        user_hit: UserDTO = UserDTO(
            user_id=UUID('00000000000000000000000000000000'), username="error", password="error", bio="error")
        for user in self.table_users:
            if user.user_id == user_id:
                user_hit = user
        return user_hit

    def get_all_users(self) -> list[UserDTO]:
        return self.table_users

    def get_user_login(self, username: str, password: str) -> UserDTO:
        user_hit: UserDTO = UserDTO(
            user_id=UUID('00000000000000000000000000000000'), username="error", password="error")
        for user in self.table_users:
            if user.username == username and user.password == password:
                user_hit = user
        return user_hit

    def insert_post(self, user_id: UUID, text: str, image: str, posted: datetime) -> PostDTO:
        new = PostDTO(post_id=uuid.uuid4(), user_id=user_id, text=text, image=image, posted=posted)
        self.table_posts.append(new)
        return PostDTO(post_id=new.post_id, user_id=new.user_id, text=new.text, image=new.image, posted=new.posted)

    def update_post(self, post_id: UUID, text: str, image: str) -> PostDTO:
        post_updated: PostDTO = PostDTO(
            post_id=UUID('00000000000000000000000000000000'), user_id=UUID('00000000000000000000000000000000'),
            text="error", image="", posted=datetime(1900, 1, 1, 1, 0))
        for post in self.table_posts:
            if post.post_id == post_id:
                post.text = text
                post.image = image
                post_updated = post
        return post_updated

    def delete_post(self, post_id: UUID) -> bool:
        success = False
        for post in self.table_posts:
            if post.post_id == post_id:
                self.table_posts.remove(post)
                success = True
        return success

    def get_post(self, post_id: UUID) -> PostDTO:
        idx_post = -1
        for idx, post in enumerate(self.table_posts):
            if post.post_id == post_id:
                idx_post = idx
        if idx_post != -1:
            return self.table_posts[idx_post]
        else:
            return PostDTO(
                post_id=UUID('00000000000000000000000000000000'), user_id=UUID('00000000000000000000000000000000'),
                text="error", image="", posted=datetime(1900, 1, 1, 1, 0))

    def get_all_posts(self) -> list[PostDTO]:
        return self.table_posts

    def get_posts_by_user(self, user_id: UUID) -> list[PostDTO]:
        posts_out: list[PostDTO] = []
        for post in self.table_posts:
            if post.user_id == user_id:
                posts_out.append(post)
        return posts_out
