using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Home
    {
        [Inject]
        public required IBusinessLayer BusinessLayer { get; set; }

        [Inject]
        public ILogger<Home> Logger { get; set; }

        private List<PostViewModel?> _postViewModelList = new();

        protected override async void OnParametersSet()
        {
            var posts = await BusinessLayer.GetAllPosts();
            _postViewModelList = posts.OrderByDescending(x => x?.DateCreated).ToList();
            try
            {
                StateHasChanged();
            }
            catch (ObjectDisposedException ex)
            {
                Logger.LogWarning($"Initializing Home: {ex.Message}");
            }
        }

        private async void OnPosted()
        {
            var newPosts = await BusinessLayer.GetAllPosts();
            var selectedPosts = newPosts.Where(x => x != null && x.DateCreated > _postViewModelList.First()?.DateCreated).ToList();
            var insertPosts = selectedPosts.OrderByDescending(x => x?.DateCreated).ToList();
            _postViewModelList.InsertRange(0, insertPosts);
            StateHasChanged();
        }
    }
}
