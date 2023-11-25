using Microsoft.AspNetCore.Components;
using Radzen;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.UserManagement
{
    public partial class Login
    {
        [Parameter] 
        public EventCallback<bool> OnRegister { get; set; }

        [Parameter]
        public EventCallback<UserViewModel> OnLoggedIn { get; set; }

        [Inject]
        public required IBusinessLayer BusinessLayer { get; set; }

        public void OnRegisterClick()
        {
            OnRegister.InvokeAsync(true);
        }

        public async void OnLoginClick(LoginArgs logArgs)
        {
            var res = await BusinessLayer.LoginUser(new UserViewModel()
            {
                Name = logArgs.Username,
                Password = logArgs.Password
            });

            if (res != null)
            {
                await OnLoggedIn.InvokeAsync(res);
            }

            //ToDo Else Validation Message
        }
    }
}
