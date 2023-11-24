using Microsoft.AspNetCore.Components;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Login
    {
        [Parameter] 
        public EventCallback<bool> OnRegister { get; set; }

        public void OnRegisterClick()
        {
            OnRegister.InvokeAsync(true);
        }
    }
}
