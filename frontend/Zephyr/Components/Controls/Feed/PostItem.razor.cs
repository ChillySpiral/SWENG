using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostItem
    {
        [Parameter]
        public PostViewModel Data { get; set; }

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
    }
}
