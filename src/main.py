from entity.post import Post
from entity.user import User, User_DTO
from repository.dbaccess import DBAccess


def main():
    ctx = DBAccess()
    user1 = User_DTO()
    user1.Id = 0
    user1.Username = "Test"
    user1.Password = "Test1"

    ctx.insert_user(user1)



if __name__ == '__main__':
    main()
