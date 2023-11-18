using Zephyr.Data.ViewModels;

namespace Zephyr.Data;

public class BusinessLayer : IBusinessLayer
{
    private List<PostViewModel> _postViewModelList;

    public BusinessLayer()
    {
        _postViewModelList = new()
        {
            new PostViewModel()
            {
                Id = 1,
                Text = "Test 1",
                User = new UserViewModel()
                {
                    Id = 1,
                    Name = "Test User 1"
                }
            },
            new PostViewModel()
            {
                Id = 2,
                Text = "Test 2",
                User = new UserViewModel()
                {
                    Id = 2,
                    Name = "Test User 2"
                }
            }
        };
    }


    public List<PostViewModel> GetAllPosts()
    {
        return _postViewModelList;
    }
}