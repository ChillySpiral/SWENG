using Microsoft.AspNetCore.Components;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Controls.Feed
{
    public partial class PostItem
    {
        [Parameter]
        public PostViewModel Data { get; set; }

        [Parameter]
        public string Style { get; set; } = "width: 400px; height: 400px; margin-left:auto; margin-right:auto;";

        [Parameter]
        public bool IsFeed { get; set; } = false;

        [Inject] 
        private NavigationManager Navigation { get; set; }

        public string SentimentIcon { get; set; } = "question_mark";

        protected override void OnParametersSet()
        {
            if (string.IsNullOrEmpty(Data.ImageUrl))
                Data.ImageUrl = null;

            if (Data.SentimentValue != null)
            {
                switch (Data.SentimentLabel)
                {
                    case PostViewModel.Sentiment.Negative:
                        SentimentIcon = "sentiment_very_dissatisfied";
                        break;
                    case PostViewModel.Sentiment.Positive:
                        SentimentIcon = "sentiment_very_satisfied";
                        break;
                    case PostViewModel.Sentiment.Neutral:
                        SentimentIcon = "sentiment_neutral";
                        break;
                    default:
                        SentimentIcon = "question_mark";
                        break;
                }
                StateHasChanged();
            }
        }

        private void NavigateToUser()
        {
            Navigation.NavigateTo($"/profile/{Data.User.Id}", true);
        }

        private void NavigateToPost()
        {
            Navigation.NavigateTo($"/post/{Data.Id}", forceLoad: true);
        }
    }
}
