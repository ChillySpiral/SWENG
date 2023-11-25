using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Home
    {
        [Inject]
        public required IBusinessLayer BusinessLayer { get; set; }

        private List<PostViewModel?> _postViewModelList = new();

        protected override async void OnInitialized()
        {
            _postViewModelList = await BusinessLayer.GetAllPosts();
            StateHasChanged();
        }

        private async void OnPosted()
        {
            _postViewModelList = await BusinessLayer.GetAllPosts();
            StateHasChanged();
        }
    }
}
