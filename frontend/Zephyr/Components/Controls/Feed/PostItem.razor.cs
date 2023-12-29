using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostItem
    {
        [Parameter]
        public PostViewModel Data { get; set; }

        [Parameter]
        public string Style { get; set; } = "width: 400px; height: 400px; margin-left:auto; margin-right:auto;";

        [Parameter]
        public bool IsFeed { get; set; } = false;

        [Inject] 
        private NavigationManager Navigation { get; set; }

        protected override void OnParametersSet()
        {
            if (string.IsNullOrEmpty(Data.ImageUrl))
                Data.ImageUrl = null;
        }

        private void NavigateToUser()
        {
            Navigation.NavigateTo($"/profile/{Data.User.Id}", true);
        }

        private void NavigateToPost()
        {
            Navigation.NavigateTo($"/post/{Data.Id}", forceLoad: true);
        }
    }
}
