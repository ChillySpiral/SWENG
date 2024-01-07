using System.Runtime.CompilerServices;

namespace Zephyr.Data.ViewModels
{
    public class PostViewModel
    {
        public Guid Id { get; set; }
        public UserViewModel User { get; set; }
        public string? Text { get; set; } = string.Empty;
        public string? ImageUrl { get; set; } = string.Empty;
        public Sentiment? SentimentLabel { get; set; } = Sentiment.Neutral;
        public string? SentimentValue { get; set; }
        public DateTimeOffset? DateCreated { get; set; }
        
        public enum Sentiment
        {
            Negative = 0,
            Neutral,
            Positive
        }
    }
}
