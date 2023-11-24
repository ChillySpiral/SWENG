using Microsoft.AspNetCore.Components;
using Radzen;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Signup
    {
        [Parameter]
        public EventCallback<bool> OnLogin { get; set; }

        public UserViewModel User { get; set; }

        public void OnRegister(LoginArgs regArgs)
        {
            Console.WriteLine("Register Clicked");
            Console.WriteLine($"Username: {regArgs.Username}");
            Console.WriteLine($"Password: {regArgs.Password}");
        }

        public void OnLoginClick()
        {
            OnLogin.InvokeAsync(true);
        }
    }
}
