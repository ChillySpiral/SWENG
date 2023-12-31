using Zephyr.Client;

namespace Zephyr.Data.ViewModels
{
    public static class Converter
    {
        #region Convert to ViewModel

        public static UserViewModel ConvertTo(this UserModel source)
        {
            return new UserViewModel()
            {
                Name = source.Username,
                Password = source.Password,
            };
        }

        public static UserViewModel ConvertTo(this UserBioModel source)
        {
            return new UserViewModel()
            {
                Name = source.Username,
                Password = source.Password,
                Bio = source.Bio
            };
        }

        public static UserViewModel ConvertTo(this UserLoginResponse source)
        {
            return new UserViewModel()
            {
                Id = source.User_id,
                Name = source.Username
            };
        }

        public static UserViewModel ConvertTo(this UserResponse source)
        {
            return new UserViewModel()
            {
                Id = source.User_id,
                Name = source.Username,
                Bio = source.Bio
            };
        }

        public static UserViewModel ConvertTo(this UserUpdateModel source)
        {
            return new UserViewModel()
            {
                Id = source.User_id,
                Name = source.Username,
                Password = source.Password,
                Bio = source.Bio
            };
        }

        public static PostViewModel ConvertTo(this PostModel source)
        {
            return new PostViewModel()
            {
                Id = source.Post_id,
                User = new UserViewModel()
                {
                    Id = source.User_id
                },
                Text = source.Text,
                ImageUrl = source.Image
            };
        }

        public static PostViewModel ConvertTo(this PostResponse source)
        {
            return new PostViewModel()
            {
                Id = source.Post_id,
                User = new UserViewModel()
                {
                    Id = source.User_id
                },
                Text = source.Text,
                ImageUrl = source.Image,
                DateCreated = source.Posted
            };
        }

        public static PostViewModel ConvertTo(this PostCreateModel source)
        {
            return new PostViewModel()
            {
                Id = Guid.Empty,
                User = new UserViewModel()
                {
                    Id = source.User_id
                },
                Text = source.Text,
                ImageUrl = source.Image
            };
        }

        public static CommentViewModel ConvertTo(this CommentResponse source)
        {
            return new CommentViewModel()
            {
                Id = source.Comment_id,
                User = new UserViewModel()
                {
                    Id = source.User_id
                },
                Text = source.Text,
                DateCreated = source.Posted
            };
        }

        public static CommentViewModel ConvertTo(this CommentCreateModel source)
        {
            return new CommentViewModel()
            {
                Id = Guid.Empty,
                PostId = source.Post_id,
                User = new UserViewModel()
                {
                    Id = source.User_id
                },
                Text = source.Text,
            };
        }

        #endregion

        #region Convert From ViewModel

        public static UserModel ConvertToUserModel(this UserViewModel source)
        {
            return new UserModel()
            {
                Username = source.Name,
                Password = source.Password,
            };
        }

        public static UserBioModel ConvertToUserBioModel(this UserViewModel source)
        {
            return new UserBioModel()
            {
                Username = source.Name,
                Password = source.Password,
                Bio = source.Bio
            };
        }

        public static UserLoginResponse ConvertToUserLoginResponse(this UserViewModel source)
        {
            return new UserLoginResponse()
            {
                User_id = source.Id,
                Username = source.Name,
                Success = true
            };
        }

        public static UserResponse ConvertToUserResponse(this UserViewModel source)
        {
            return new UserResponse()
            {
                User_id = source.Id,
                Username = source.Name,
                Bio = source.Bio
            };
        }

        public static UserUpdateModel ConvertToUserUpdateModel(this UserViewModel source)
        {
            return new UserUpdateModel()
            {
                User_id = source.Id,
                Username = source.Name,
                Password = source.Password,
                Bio = source.Bio
            };
        }

        public static PostModel ConvertToPostModel(this PostViewModel source)
        {
            return new PostModel()
            {
                Post_id = source.Id,
                User_id = source.User.Id,
                Text = source.Text,
                Image = source.ImageUrl
            };
        }

        public static PostCreateModel ConvertToPostCreateModel(this PostViewModel source)
        {
            return new PostCreateModel()
            {
                User_id = source.User.Id,
                Text = source.Text,
                Image = source.ImageUrl
            };
        }

        public static PostResponse ConvertToPostResponse(this PostViewModel source)
        {
            return new PostResponse()
            {
                Post_id = source.Id,
                User_id = source.User.Id,
                Text = source.Text,
                Image = source.ImageUrl,
                Posted = source.DateCreated.Value
            };
        }

        public static CommentCreateModel ConvertToCommentCreateModel(this CommentViewModel source)
        {
            return new CommentCreateModel()
            {
                Post_id = source.PostId,
                User_id = source.User.Id,
                Text = source.Text,
            };
        }

        public static CommentResponse ConvertToCommentResponse(this CommentViewModel source)
        {
            return new CommentResponse()
            {
                Comment_id = source.Id,
                Post_id = source.Id,
                User_id = source.User.Id,
                Text = source.Text,
                Posted = source.DateCreated.Value
            };
        }

        #endregion
    }
}
