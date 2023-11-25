using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;
using Zephyr.Services;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostInput
    {
        [Parameter] 
        public EventCallback OnPosted { get; set; }

        [Inject]
        public IBusinessLayer BusinessLayer { get; set; }

        [Inject]
        public required ISessionStorageService SessionStorageService { get; set; }

        [Inject]
        public required IEventService EventService { get; set; }

        protected override void OnAfterRender(bool firstRender)
        {
            EventService.LoginEvent += OnUserLogInChange;
            CheckIfLoggedIn();
        }

        public bool UserLoggedIn { get; set; } = false;

        private string Text { get; set; } = string.Empty;

        private string? ImageUrl { get; set; } = null;

        private Guid? UserId { get; set; }

        public async void OnUserLogInChange(object? sender, bool isLoggedIn)
        {
            if (isLoggedIn)
            {
                var user = await SessionStorageService.GetItemAsync<UserViewModel>("user");
                if (user != null)
                {
                    await InvokeAsync(() =>
                    {
                        UserId = user.Id;
                        UserLoggedIn = true;
                        StateHasChanged();
                    });
                }
                else
                {
                    UserId = null;
                }
            }
            else
            {
                await InvokeAsync(() =>
                {
                    UserId = null;
                    UserLoggedIn = false;
                    StateHasChanged();
                });
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
                    UserId = user.Id;
                    UserLoggedIn = true;
                    StateHasChanged();
                }
            }
            else if (UserLoggedIn && !userSessionActive)
            {
                UserId = null;
                UserLoggedIn = false;
                StateHasChanged();
            }
        }

        private async void OnPost()
        {
            if (!UserLoggedIn || UserId == null)
                return;

            var newPost = new PostViewModel()
            {
                User = new UserViewModel()
                {
                    Id = UserId.Value,
                },
                ImageUrl = ImageUrl ?? string.Empty,
                Text = Text
            };

            await BusinessLayer.AddPost(newPost);
            await OnPosted.InvokeAsync();

            ImageUrl = null;
            Text = "";
            StateHasChanged();
        }

    }
}
