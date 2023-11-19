using Zephyr.Data.ViewModels;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    private List<PostViewModel> _postViewModelList;
    private List<UserViewModel> _userViewModelList;

    public BusinessLayer()
    {
        var user1 = new UserViewModel()
        {
            Id = 1,
            Name = "Test User 1",
            Bio = "I am User one"
        };        
        
        var user2 = new UserViewModel()
        {
            Id = 2,
            Name = "Test User 2",
            Bio = "I am User two"
        };

        _userViewModelList = new List<UserViewModel>
        {
            user1,
            user2
        };

        _postViewModelList = new()
        {
            new PostViewModel()
            {
                Id = 1,
                Text = "Test 1",
                User = user1
            },
            new PostViewModel()
            {
                Id = 2,
                Text = "Test 2",
                User = user2
            },
            new PostViewModel()
            {
                Id = 3,
                Text = "Test 3",
                User = user1
            },
            new PostViewModel()
            {
                Id = 4,
                Text = "Test 4",
                User = user2
            },
            new PostViewModel()
            {
                Id = 5,
                Text = "Test 5",
                User = user1
            },
            new PostViewModel()
            {
                Id = 6,
                Text = "Test 6",
                User = user2
            }
        };
    }


    public List<PostViewModel> GetAllPosts()
    {
        var res = _postViewModelList.ToList();
        res.Reverse();
        return res;
    }

    public List<PostViewModel> GetUserPosts(int UserId)
    {
        var res = _postViewModelList.Where(x => x.User.Id.Equals(UserId)).ToList();
        res.Reverse();
        return res;
    }

    public UserViewModel GetUser(int UserId)
    {
        return _userViewModelList.First(x => x.Id.Equals(UserId));
    }

    public void AddPost(PostViewModel post)
    {
        post.User = GetUser(post.User.Id);
        post.Id = _postViewModelList.Count + 1;
        _postViewModelList.Add(post);
    }
}