using Zephyr.Data.ViewModels;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    private Client.Client Client { get; set; } = new("127.0.0.1:8000", new HttpClient());

    public async Task<UserViewModel?> GetUser(Guid userId)
    {
        var response = await Client.UserGetAsync(userId);
        return response?.ConvertTo();
    }

    public async Task<UserViewModel?> CreateUser(UserViewModel newUser)
    {
        var response = await Client.UserPostAsync(newUser.ConvertToUserBioModel());
        return response?.ConvertTo();
    }

    public async Task<UserViewModel?> UpdateUser(UserViewModel user)
    {
        var response = await Client.UserPutAsync(user.ConvertToUserUpdateModel());
        return response?.ConvertTo();
    }

    public async Task<bool> DeleteUser(Guid userId)
    {
        var response = await Client.UserDeleteAsync(userId);
        return response;
    }

    public async Task<UserViewModel?> LoginUser(UserViewModel user)
    {
        var response = await Client.UserLoginAsync(user.ConvertToUserModel());
        return response.Success ? response.ConvertTo() : null;
    }

    public async Task<List<UserViewModel?>> GetAllUser()
    {
        var response = await Client.UsersAsync();
        var res = new List<UserViewModel?>();
        if (response is { Count: > 0 }) 
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));
        return res;
    }

    public async Task<PostViewModel?> AddPost(PostViewModel post)
    {
        var response = await Client.PostPostAsync(post.ConvertToPostCreateModel());
        return response.ConvertTo();
    }

    public async Task<PostViewModel?> UpdatePost(PostViewModel post)
    {
        var response = await Client.PostPutAsync(post.ConvertToPostModel());
        return response.ConvertTo();
    }

    public async Task<PostViewModel?> GetPost(Guid postId)
    {
        var response = await Client.PostGetAsync(postId);
        return response.ConvertTo();
    }

    public async Task<bool> RemovePost(Guid postId)
    {
        var response = await Client.PostDeleteAsync(postId);
        return response;
    }

    public async Task<List<PostViewModel?>> GetAllPosts()
    {
        var response = await Client.PostsAsync();
        var res = new List<PostViewModel?>();
        if (response is { Count: > 0 })
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));
        return res;
    }

    public async Task<List<PostViewModel?>> GetUserPosts(Guid userId)
    {
        var response = await Client.PostsUserAsync(userId);
        var res = new List<PostViewModel?>();
        if (response is { Count: > 0 })
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));
        return res;
    }

    public async Task<PostViewModel?> GetNewestPost()
    {
        var response = await Client.PostNewestAsync();
        return response.ConvertTo();
    }
}