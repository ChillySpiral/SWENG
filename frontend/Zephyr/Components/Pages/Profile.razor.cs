using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Profile
    {
        [Parameter]
        public Guid UserId { get; set; }

        [Inject]
        public IBusinessLayer BusinessLayer { get; set; }

        private List<PostViewModel?> _postViewModelList = new();
        private UserViewModel? _userViewModel;

        public bool IsLoading { get; set; } = true;

        public Profile() { }

        protected override async void OnParametersSet()
        {
            _userViewModel = await BusinessLayer.GetUser(UserId);
            _postViewModelList = await BusinessLayer.GetUserPosts(UserId);
            IsLoading = false;
            StateHasChanged();
        }
    }
}
