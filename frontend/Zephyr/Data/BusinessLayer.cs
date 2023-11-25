using Zephyr.Data.ViewModels;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    public BusinessLayer()
    {

    }

    public UserViewModel? GetUser(int userId)
    {
        throw new NotImplementedException();
    }

    public UserViewModel? CreateUser(UserViewModel newUser)
    {
        throw new NotImplementedException();
    }

    public UserViewModel? UpdateUser(UserViewModel user)
    {
        throw new NotImplementedException();
    }

    public UserViewModel? DeleteUser(int userId)
    {
        throw new NotImplementedException();
    }

    public UserViewModel? LoginUser(string username, string password)
    {
        throw new NotImplementedException();
    }

    public List<UserViewModel?> GetAllUser()
    {
        throw new NotImplementedException();
    }

    public PostViewModel? AddPost(PostViewModel post)
    {
        throw new NotImplementedException();
    }

    public PostViewModel? UpdatePost(PostViewModel post)
    {
        throw new NotImplementedException();
    }

    public PostViewModel? GetPost(int postId)
    {
        throw new NotImplementedException();
    }

    public void RemovePost(int postId)
    {
        throw new NotImplementedException();
    }

    public List<PostViewModel> GetAllPosts()
    {
        throw new NotImplementedException();
    }

    public List<PostViewModel> GetUserPosts(int userId)
    {
        throw new NotImplementedException();
    }

    public PostViewModel? GetNewestPost()
    {
        throw new NotImplementedException();
    }
}