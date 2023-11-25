using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;
using Zephyr.Services;

namespace Zephyr.Components.Pages
{
    public partial class Signin
    {
        [Inject]
        private NavigationManager Navigation { get; set; }

        [Inject]
        public required ISessionStorageService SessionStorageService { get; set; }

        [Inject]
        public required IEventService EventService { get; set; }

        public bool IsLogin { get; set; } = true;
        public bool UserLoggedIn { get; set; } = false;

        protected override async void OnParametersSet()
        {
            if (await SessionStorageService.ContainKeyAsync("user"))
            {
                UserLoggedIn = true;
                StateHasChanged();
            }
        }

        public void OnRegisterNavigation(bool change)
        {
            if (change)
            {
                IsLogin = false;
                StateHasChanged();
            }
        }

        public void OnLoginNavigation(bool change)
        {
            if (change)
            {
                IsLogin = true;
                StateHasChanged();
            }
        }

        public async void OnUserLoggedIn(UserViewModel loggedUser)
        {
            await SessionStorageService.SetItemAsync("user", loggedUser);
            EventService.RaiseLoginEvent(true);
            UserLoggedIn = true;
            Navigation.NavigateTo("/");
        }
    }
}
