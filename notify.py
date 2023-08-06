import sys
import os
from notifypy import Notify

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(application_path, 'assets', 'icon.png')
audio_path = os.path.join(application_path, 'assets', 'notification.wav')

def notify_event(event_name, event_description):
    notification = Notify()
    notification.title = event_name
    notification.message = event_description
    notification.icon = icon_path
    notification.audio = audio_path
    notification.application_name = 'Schedule Events'
    notification.send()
