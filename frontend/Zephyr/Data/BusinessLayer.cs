using Zephyr.Data.ViewModels;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    private Client.Client ServerClient { get; set; } 
    private readonly IConfiguration _config;

    public BusinessLayer(IConfiguration config)
    {
        _config = config;
        var baseUrl = _config.GetValue<string>("Connection:Server");
        ServerClient = new Client.Client(baseUrl, new HttpClient());
    }

    public async Task<UserViewModel?> GetUser(Guid userId)
    {
        var response = await ServerClient.UserGetAsync(userId);
        return response?.ConvertTo();
    }

    public async Task<UserViewModel?> CreateUser(UserViewModel newUser)
    {
        var response = await ServerClient.UserPostAsync(newUser.ConvertToUserBioModel());
        return response?.ConvertTo();
    }

    public async Task<UserViewModel?> UpdateUser(UserViewModel user)
    {
        var response = await ServerClient.UserPutAsync(user.ConvertToUserUpdateModel());
        return response?.ConvertTo();
    }

    public async Task<bool> DeleteUser(Guid userId)
    {
        var response = await ServerClient.UserDeleteAsync(userId);
        return response;
    }

    public async Task<UserViewModel?> LoginUser(UserViewModel user)
    {
        var response = await ServerClient.UserLoginAsync(user.ConvertToUserModel());
        return response.Success ? response.ConvertTo() : null;
    }

    public async Task<List<UserViewModel?>> GetAllUser()
    {
        var response = await ServerClient.UsersAsync();
        var res = new List<UserViewModel?>();
        if (response is { Count: > 0 }) 
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));
        return res;
    }

    public async Task<PostViewModel?> AddPost(PostViewModel post)
    {
        var response = await ServerClient.PostPostAsync(post.ConvertToPostCreateModel());
        return response.ConvertTo();
    }

    public async Task<PostViewModel?> UpdatePost(PostViewModel post)
    {
        var response = await ServerClient.PostPutAsync(post.ConvertToPostModel());
        return response.ConvertTo();
    }

    public async Task<PostViewModel?> GetPost(Guid postId)
    {
        var response = await ServerClient.PostGetAsync(postId);
        return response.ConvertTo();
    }

    public async Task<bool> RemovePost(Guid postId)
    {
        var response = await ServerClient.PostDeleteAsync(postId);
        return response;
    }

    public async Task<List<PostViewModel?>> GetAllPosts()
    {
        var response = await ServerClient.PostsAsync();
        var res = new List<PostViewModel?>();
        if (response is { Count: > 0 })
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));

        var userDict = new Dictionary<Guid, UserViewModel>();
        foreach (var post in res)
        {
            userDict.TryGetValue(post.User.Id, out var user);
            if(user == null)
            {
                user = await GetUser(post.User.Id);
                if(user != null)
                    userDict.Add(post.User.Id, user);
            }
            post.User = user;
        }

        return res;
    }

    public async Task<List<PostViewModel?>> GetUserPosts(UserViewModel user)
    {
        var response = await ServerClient.PostsUserAsync(user.Id);
        var res = new List<PostViewModel?>();
        if (response is { Count: > 0 })
            res.AddRange(response.Select(userResponse => userResponse.ConvertTo()));
        res.ForEach(x =>
        {
            if (x != null) 
                x.User = user;
        });
        return res;
    }

    public async Task<PostViewModel?> GetNewestPost()
    {
        var response = await ServerClient.PostNewestAsync();
        return response.ConvertTo();
    }


    private List<CommentViewModel> _tempComments = new List<CommentViewModel>()
    {
        new CommentViewModel()
        {
            User = new UserViewModel()
            {
                Name = "User 1"
            },
            Text = "Test 1 Comment",
            DateCreated = DateTimeOffset.Now
        },
        new CommentViewModel()
        {
            User = new UserViewModel()
            {
                Name = "User 2"
            },
            Text = "Test 2 Comment",
            DateCreated = DateTimeOffset.Now
        }
    };

    public async Task<List<CommentViewModel?>> GetPostComments(Guid postId)
    {
        return _tempComments;
    }

    public async Task<CommentViewModel?> AddComment(CommentViewModel comment)
    {
        _tempComments.Add(comment);
        return comment;
    }

}