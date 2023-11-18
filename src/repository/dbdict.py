from src.entity.user import UserDTO
from src.entity.post import PostDTO


class DBAccess:
    # Singleton Class DBAccess
    _instance = None
    __data_dict = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBAccess, cls).__new__(cls)
        return cls._instance

    def __int__(self):
        self.__data_dict = {}

    def insert_post(self, post: PostDTO):
        self.__data_dict["post" + str(post.post_id)] = post

    def insert_user(self, user: UserDTO):
        self.__data_dict["user" + str(user.user_id)] = user

    def get_user(self, id: int) -> UserDTO:
        return self.__data_dict["user" + str(id)]

    def get_post(self, id: int) -> UserDTO:
        return self.__data_dict["post" + str(id)]

    def get_all_posts(self):
        return [value for key, value in self.__data_dict.items() if "post" in key]

    def get_all_users(self):
        return [value for key, value in self.__data_dict.items() if "user" in key]
