using Zephyr.Data.ViewModels;

namespace Zephyr.Data
{
    public interface IBusinessLayer
    {
        public List<PostViewModel> GetAllPosts();

        public List<PostViewModel> GetUserPosts(int UserId);

        public UserViewModel GetUser(int UserId);
    }
}
