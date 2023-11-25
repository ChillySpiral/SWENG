using Zephyr.Data.ViewModels;
using Zephyr.Client;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    private Client.Client? Client { get; set; } = new("127.0.0.1:8000", new HttpClient());

    public UserViewModel? GetUser(Guid userId)
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

    public UserViewModel? DeleteUser(Guid userId)
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

    public PostViewModel? GetPost(Guid postId)
    {
        throw new NotImplementedException();
    }

    public void RemovePost(Guid postId)
    {
        throw new NotImplementedException();
    }

    public List<PostViewModel> GetAllPosts()
    {
        throw new NotImplementedException();
    }

    public List<PostViewModel> GetUserPosts(Guid userId)
    {
        throw new NotImplementedException();
    }

    public PostViewModel? GetNewestPost()
    {
        throw new NotImplementedException();
    }
}