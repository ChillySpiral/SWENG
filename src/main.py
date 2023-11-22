from src.entity.post import PostDTO
from src.entity.user import UserDTO
from repository.db_access import DBAccess


def main():
    ctx = DBAccess()
    ctx.insert_post(PostDTO(post_id=1, user_id=1))
    ctx.insert_user(UserDTO(user_id=1))
    print(PostDTO.list_as_json(ctx.get_all_posts()))


if __name__ == '__main__':
    main()
