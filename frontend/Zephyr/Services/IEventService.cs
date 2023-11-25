namespace Zephyr.Services
{
    public interface IEventService
    {
        event EventHandler<bool> LoginEvent;
        public void RaiseLoginEvent(bool isLoggedIn);
    }

    public class EventService : IEventService
    {
        public event EventHandler<bool> LoginEvent;

        public void RaiseLoginEvent(bool isLoggedIn)
        {
            LoginEvent.Invoke(this, isLoggedIn);
        }
    }
}
