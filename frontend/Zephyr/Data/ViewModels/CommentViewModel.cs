namespace Zephyr.Data.ViewModels
{
    public class CommentViewModel
    {
        public Guid Id { get; set; }
        public Guid PostId { get; set; }
        public UserViewModel User { get; set; }
        public string? Text { get; set; } = string.Empty;
        public DateTimeOffset? DateCreated { get; set; }
    }
}
