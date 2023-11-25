using Microsoft.AspNetCore.Components;
using Radzen;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Signup
    {
        [Parameter]
        public EventCallback<bool> OnLogin { get; set; }

        [Parameter]
        public EventCallback<UserViewModel> OnLoggedIn { get; set; }

        [Inject]
        public required IBusinessLayer BusinessLayer { get; set; }

        public UserViewModel User { get; set; }

        public async void OnRegister(LoginArgs regArgs)
        {
            var res = await BusinessLayer.CreateUser(new UserViewModel()
            {
                Name = regArgs.Username,
                Password = regArgs.Password
            });

            if (res != null)
            {
                await OnLoggedIn.InvokeAsync(res);
            }

            //ToDo: Else Validation Message
        }

        public void OnLoginClick()
        {
            OnLogin.InvokeAsync(true);
        }
    }
}
