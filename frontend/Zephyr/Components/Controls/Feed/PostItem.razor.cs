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

        private void NavigateToUser()
        {
            Navigation.NavigateTo($"/profile/{Data.User.Id}", true);
        }
    }
}
