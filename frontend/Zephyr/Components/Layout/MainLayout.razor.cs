namespace Zephyr.Components.Layout
{
    public partial class MainLayout
    {
        public bool SidebarExpanded;

        private void ToggleSidebar()
        {
            SidebarExpanded = !SidebarExpanded;
        }
    }
}
