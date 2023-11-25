using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Profile
    {
        [Parameter]
        public string UserId
        {
            get => _userId.ToString();
            set
            {
                if (Guid.TryParse(value, out _userId))
                {

                }
            }
        }

        [Inject]
        public IBusinessLayer BusinessLayer { get; set; }

        private Guid _userId;
        private List<PostViewModel?> _postViewModelList = new();
        private UserViewModel? _userViewModel;

        public bool IsLoading { get; set; } = true;

        public Profile() { }

        protected override async void OnParametersSet()
        {
            _userViewModel = await BusinessLayer.GetUser(_userId);
            _postViewModelList = await BusinessLayer.GetUserPosts(_userId);
            IsLoading = false;
            StateHasChanged();
        }
    }
}
