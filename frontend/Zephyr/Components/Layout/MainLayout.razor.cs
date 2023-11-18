namespace Zephyr.Components.Layout
{
    public partial class MainLayout
    {
        bool _sidebarExpanded = false;

        private void ToggleSidebar()
        {
            _sidebarExpanded = !_sidebarExpanded;
            StateHasChanged();
        }
    }
}
