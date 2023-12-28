using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Post
    {
        [Parameter]
        public string PostId
        {
            get => _postId.ToString();
            set
            {
                if (Guid.TryParse(value, out _postId))
                {

                }
            }
        }

        [Inject]
        public IBusinessLayer BusinessLayer { get; set; }

        private PostViewModel _postViewModel { get; set; }
        private List<CommentViewModel> _comments = new List<CommentViewModel>();
        private Guid _postId;

        public bool IsLoading { get; set; } = true;

        public Post() { }

        protected override async void OnParametersSet()
        {
            _postViewModel = await BusinessLayer.GetPost(_postId) ?? new PostViewModel()
            {
                Id = _postId,
            };

            if (_postViewModel?.User.Id != null)
            {
                _postViewModel.User = await BusinessLayer.GetUser(_postViewModel.User.Id);
            }

            if (_postViewModel != null)
            {
                _comments = await BusinessLayer.GetPostComments(_postViewModel.Id);
            }

            IsLoading = false;
            StateHasChanged();
        }

        private async void OnPosted()
        {
            var newComments = await BusinessLayer.GetPostComments(_postId);
            var selectedComments = newComments.Where(x => x != null && x.DateCreated > _comments.First()?.DateCreated && !_comments.Contains(x)).ToList();
            var insertComments = selectedComments.OrderByDescending(x => x?.DateCreated).ToList();
            _comments.InsertRange(0, insertComments);
            StateHasChanged();
        }
    }
}
