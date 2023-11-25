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
        public IBusinessLayer? BusinessLayer { get; set; }

        private List<PostViewModel> _postViewModelList = new();
        private UserViewModel _userViewModel;

        public bool IsLoading { get; set; } = true;

        public Profile() { }

        protected override void OnParametersSet()
        {
            _userViewModel = BusinessLayer.GetUser(UserId);
            _postViewModelList = BusinessLayer.GetUserPosts(UserId);
            IsLoading = false;
            StateHasChanged();
        }
    }
}
