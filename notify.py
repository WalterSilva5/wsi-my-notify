from notifypy import Notify

def notify_event(event_name, event_description):
    notification = Notify()
    notification.title = event_name
    notification.message = event_description
    notification.icon = 'assets/icon.png'
    notification.audio = 'assets/notification.wav'
    notification.application_name = 'Schedule Events'
    notification.send()


if __name__ == '__main__':
    notify_event('Test', 'Notification test')