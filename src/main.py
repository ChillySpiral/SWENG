from repository.dbdict import DBAccess
from src.entity.post import PostDTO
from src.entity.user import UserDTO


def main():
    ctx = DBAccess()
    ctx.insert_post(PostDTO(1))
    ctx.insert_user(UserDTO(1))
    print(ctx.get_user(1).Id)

if __name__ == '__main__':
    main()
