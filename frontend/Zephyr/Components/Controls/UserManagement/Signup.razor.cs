using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Signup
    {
        [Parameter]
        public EventCallback<bool> OnLogin { get; set; }

        public UserViewModel User { get; set; }

        public void OnLoginClick()
        {
            OnLogin.InvokeAsync(true);
        }
    }
}
