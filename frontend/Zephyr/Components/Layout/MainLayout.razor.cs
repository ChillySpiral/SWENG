using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;
using Zephyr.Services;

namespace Zephyr.Components.Layout
{
    public partial class MainLayout
    {
        [Inject]
        public required ISessionStorageService SessionStorageService { get; set; }

        [Inject]
        public required IEventService EventService { get; set; }

        protected override void OnAfterRender(bool firstRender)
        {
            EventService.LoginEvent += OnUserLogInChange;
            CheckIfLoggedIn();
        }

        public bool SidebarExpanded;

        public bool UserLoggedIn { get; set; } = false; 

        public string? UserName { get; set; }
        public string? UserPath { get; set; }

        public async void OnUserLogInChange(object? sender, bool isLoggedIn)
        {
            if (isLoggedIn)
            {
                var user = await SessionStorageService.GetItemAsync<UserViewModel>("user");
                if (user != null)
                {
                    UserName = user.Name;
                    UserPath = $"profile/{user.Id}";
                    UserLoggedIn = true;
                    StateHasChanged();
                }
            }
            else
            {
                UserLoggedIn = false;
                UserName = null;
                UserPath = null;
                StateHasChanged();
            }
        }

        private async void CheckIfLoggedIn()
        {
            var userSessionActive = await SessionStorageService.ContainKeyAsync("user");
            if (!UserLoggedIn && userSessionActive)
            {
                var user = await SessionStorageService.GetItemAsync<UserViewModel>("user");
                if (user != null)
                {
                    UserName = user.Name;
                    UserPath = $"profile/{user.Id}";
                    UserLoggedIn = true;
                    StateHasChanged();
                }
            }
            else if (UserLoggedIn && !userSessionActive)
            {
                UserLoggedIn = false;
                UserName = null;
                UserPath = null;
                StateHasChanged();
            }
        }

        private void ToggleSidebar()
        {
            SidebarExpanded = !SidebarExpanded;
        }
    }
}
