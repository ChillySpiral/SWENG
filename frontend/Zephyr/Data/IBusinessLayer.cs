using Zephyr.Data.ViewModels;

namespace Zephyr.Data
{
    public interface IBusinessLayer
    {
        #region User

        public UserViewModel? GetUser(int userId);
        public UserViewModel? CreateUser(UserViewModel newUser);
        public UserViewModel? UpdateUser(UserViewModel user);
        public UserViewModel? DeleteUser(int userId);
        public UserViewModel? LoginUser(string username, string password);
        public List<UserViewModel?> GetAllUser();

        #endregion

        #region Post

        public PostViewModel? AddPost(PostViewModel post);
        public PostViewModel? UpdatePost(PostViewModel post);
        public PostViewModel? GetPost(int postId);
        public void RemovePost(int postId);
        public List<PostViewModel> GetAllPosts();
        public List<PostViewModel> GetUserPosts(int userId);
        public PostViewModel? GetNewestPost();

        #endregion
    }
}
