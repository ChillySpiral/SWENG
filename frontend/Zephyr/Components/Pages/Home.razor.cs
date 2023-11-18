using Microsoft.AspNetCore.Components;
using Zephyr.Data;
using Zephyr.Data.ViewModels;

namespace Zephyr.Components.Pages
{
    public partial class Home
    {
        [Inject]
        private IBusinessLayer _businessLayer { get; set; }

        private List<PostViewModel> _postViewModelList = new();

        protected override void OnInitialized()
        {
            _postViewModelList = _businessLayer.GetAllPosts();
        }
    }
}
