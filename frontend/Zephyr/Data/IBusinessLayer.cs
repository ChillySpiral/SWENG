using Zephyr.Data.ViewModels;

namespace Zephyr.Data
{
    public interface IBusinessLayer
    {
        #region User

        public UserViewModel? GetUser(Guid userId);
        public UserViewModel? CreateUser(UserViewModel newUser);
        public UserViewModel? UpdateUser(UserViewModel user);
        public UserViewModel? DeleteUser(Guid userId);
        public UserViewModel? LoginUser(string username, string password);
        public List<UserViewModel?> GetAllUser();

        #endregion

        #region Post

        public PostViewModel? AddPost(PostViewModel post);
        public PostViewModel? UpdatePost(PostViewModel post);
        public PostViewModel? GetPost(Guid postId);
        public void RemovePost(Guid postId);
        public List<PostViewModel> GetAllPosts();
        public List<PostViewModel> GetUserPosts(Guid userId);
        public PostViewModel? GetNewestPost();

        #endregion
    }
}
