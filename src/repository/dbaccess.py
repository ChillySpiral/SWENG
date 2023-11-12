from sqliteframe import Database, table, String, Integer, Boolean, ForeignKey
from pathlib import Path

from src.entity.post import Post, Post_DTO
from src.entity.user import User, User_DTO

database = Database(Path("sweng.db"), output=True)


class DBAccess:

    def insert_user(self, user: User_DTO):
        insert_statement = User.insert_into(
            {User.id: user.Id, User.username: user.Username, User.password: user.Password})
        with database.connection(commit=True):
            res = insert_statement.execute()
            print(res)

    def get_user(self, id: Integer):
        select_statement = User.select().where(User.Id == id)
        with database.connection(commit=True):
            res = select_statement.execute()
            print(res)

    def insert_post(self, post: Post_DTO):
        insert_statement = Post.insert_into({Post.user_id: post.user_id, Post.text: post.text, Post.image: post.image})
        with database.connection(commit=True):
            res = insert_statement.execute()
            print(res)

    def get_post(self, id: Integer):
        select_statement = Post.select().where(Post.Id == id)
        with database.connection(commit=True):
            res = select_statement.execute()
            print(res)
