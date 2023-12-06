using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Microsoft.JSInterop;
using Zephyr.Services;

namespace Zephyr.Components.Pages
{
    public partial class Logout
    {
        [Inject]
        private NavigationManager Navigation { get; set; }

        [Inject]
        public required ISessionStorageService SessionStorageService { get; set; }

        [Inject]
        public required IEventService EventService { get; set; }


        protected override async void OnInitialized()
        {
            try
            {
                if (await SessionStorageService.ContainKeyAsync("user"))
                {
                    await SessionStorageService.RemoveItemAsync("user");
                    EventService.RaiseLoginEvent(false);
                    Navigation.NavigateTo("/");
                }
            }
            catch (JSDisconnectedException e)
            {
                //Ignore
            }
        }
    }
}
