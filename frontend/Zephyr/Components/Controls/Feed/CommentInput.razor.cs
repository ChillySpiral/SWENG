using Blazored.SessionStorage;
using Microsoft.AspNetCore.Components;
using Microsoft.JSInterop;
using Zephyr.Data.ViewModels;
using Zephyr.Data;
using Zephyr.Services;

namespace Zephyr.Components.Controls.Feed
{
    public partial class CommentInput
    {
        [Parameter] public EventCallback OnPosted { get; set; }

        [Parameter]
        public Guid PostId { get; set; }

        [Inject] public IBusinessLayer BusinessLayer { get; set; }

        [Inject] public required ISessionStorageService SessionStorageService { get; set; }

        [Inject] public required IEventService EventService { get; set; }

        protected override void OnAfterRender(bool firstRender)
        {
            EventService.LoginEvent += OnUserLogInChange;
            CheckIfLoggedIn();
        }

        public bool UserLoggedIn { get; set; } = false;

        public bool IsBusy { get; set; } = false;

        private string Text { get; set; } = string.Empty;

        private Guid? UserId { get; set; }

        public async void OnUserLogInChange(object? sender, bool isLoggedIn)
        {
            try
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
            catch (JSDisconnectedException ex)
            {
                // Ignore
            }
        }

        private async void CheckIfLoggedIn()
        {
            try
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
            catch (JSDisconnectedException ex)
            {
                // Ignore
            }

        }

        private async void OnPost()
        {
            try
            {
                if (!UserLoggedIn || UserId == null)
                    return;

                var newComment = new CommentViewModel()
                {
                    PostId = PostId,
                    User = new UserViewModel()
                    {
                        Id = UserId.Value,
                    },
                    Text = Text
                };

                await BusinessLayer.AddComment(newComment);
                await OnPosted.InvokeAsync();

                Text = "";
                StateHasChanged();
            }
            catch (JSDisconnectedException ex)
            {
                // Ignore
            }
        }

        private async void OnGenerate()
        {
            try
            {
                if (!UserLoggedIn || UserId == null)
                    return;
                IsBusy = true;
                var output = await BusinessLayer.GenerateComment(PostId, Text);

                Text = output ?? string.Empty;
                IsBusy = false;
                StateHasChanged();
            }
            catch (JSDisconnectedException ex)
            {
                // Ignore
            }
        }

    }
}


