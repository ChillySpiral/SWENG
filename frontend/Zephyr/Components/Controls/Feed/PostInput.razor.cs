﻿using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostInput
    {
        [Parameter] 
        public EventCallback OnPosted { get; set; }

        [Inject]
        public IBusinessLayer BusinessLayer { get; set; }

        private string Text { get; set; } = string.Empty;

        public string? ImageUrl { get; set; } = null;

        private async void OnPost()
        {
            var newPost = new PostViewModel()
            {
                User = new UserViewModel()
                {
                    Id = 1
                },
                ImageUrl = ImageUrl,
                Text = Text
            };

            BusinessLayer.AddPost(newPost);
            await OnPosted.InvokeAsync();

            ImageUrl = null;
            Text = "";
            StateHasChanged();
        }
    }
}