using System.Runtime.CompilerServices;

namespace Zephyr.Data.ViewModels
{
    public class PostViewModel
    {
        public Guid Id { get; set; }
        public UserViewModel User { get; set; }
        public string? Text { get; set; }

        public string? ImageUrl { get; set; }
        public DateTimeOffset? DateCreated { get; set; }
        
    }
}
