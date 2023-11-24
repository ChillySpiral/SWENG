namespace Zephyr.Components.Pages
{
    public partial class Signin
    {
        public bool IsLogin { get; set; } = true;

        public void OnRegisterNavigation(bool change)
        {
            if (change)
            {
                IsLogin = false;
                StateHasChanged();
            }
        }

        public void OnLoginNavigation(bool change)
        {
            if (change)
            {
                IsLogin = true;
                StateHasChanged();
            }
        }
    }
}
