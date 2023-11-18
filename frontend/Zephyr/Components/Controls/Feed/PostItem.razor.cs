using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostItem
    {
        [Parameter]
        public PostViewModel Data { get; set; }

    }
}
