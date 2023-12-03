using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class User
    {
        [Parameter]
        public UserViewModel UserData { get; set; }


    }
}
