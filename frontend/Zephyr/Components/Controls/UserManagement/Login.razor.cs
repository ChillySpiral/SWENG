using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Radzen;
using Zephyr.Data;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Login
    {
        [Parameter] 
        public EventCallback<bool> OnRegister { get; set; }

        [Inject]
        public ISessionStorageService? SessionStorageService { get; set; }

        [Inject]
        public IBusinessLayer? BusinessLayer { get; set; }

        public void OnRegisterClick()
        {
            OnRegister.InvokeAsync(true);
        }

        public void OnLoginClick(LoginArgs logArgs)
        {
            Console.WriteLine("Login Clicked");
            Console.WriteLine($"Username: {logArgs.Username}");
            Console.WriteLine($"Password: {logArgs.Password}");

            //ToDo Send Login Data
        }
    }
}
