using Microsoft.AspNetCore.Components;

namespace Zephyr.Components.Pages
{
    public partial class Profile
    {
        [Parameter]
        public Guid UserId { get; set; }

        public Profile() { }


    }
}
