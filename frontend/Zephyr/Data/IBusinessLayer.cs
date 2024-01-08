using Zephyr.Data.ViewModels;

namespace Zephyr.Data
{
    public interface IBusinessLayer
    {
        #region User

        public Task<UserViewModel?> GetUser(Guid userId);
        public Task<UserViewModel?> CreateUser(UserViewModel newUser);
        public Task<UserViewModel?> UpdateUser(UserViewModel user);
        public Task<bool> DeleteUser(Guid userId);
        public Task<UserViewModel?> LoginUser(UserViewModel user);
        public Task<List<UserViewModel?>> GetAllUser();

        #endregion

        #region Post

        public Task<PostViewModel?> AddPost(PostViewModel post);
        public Task<PostViewModel?> UpdatePost(PostViewModel post);
        public Task<PostViewModel?> GetPost(Guid postId);
        public Task<bool> RemovePost(Guid postId);
        public Task<List<PostViewModel?>> GetAllPosts();
        public Task<List<PostViewModel?>> GetUserPosts(UserViewModel user);
        public Task<PostViewModel?> GetNewestPost();

        #endregion

        #region Comment

        public Task<List<CommentViewModel?>> GetPostComments(Guid postId);
        public Task<CommentViewModel?> AddComment(CommentViewModel comment);
        public Task<string?> GenerateComment(Guid postId,  string comment); 

        #endregion
    }
}
