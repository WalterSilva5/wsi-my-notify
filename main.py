from time import sleep, ctime, time
from notifypy import Notify
import json
import os

schedule_events_file = 'schedule_events.json'

def get_current_time():
    current_time = time()
    current_time = ctime(current_time)
    current_time = current_time.split(' ')[4]
    current_time = current_time.split(':')
    current_hour, current_minute, current_second = [int(i) for i in current_time]
    return current_hour, current_minute, current_second

def notify_event(event_name, event_description):
    notification = Notify()
    notification.title = event_name
    notification.message = event_description
    notification.send()

def get_schedule_events():
    schedule_events_obj = []
    
    if os.path.exists(schedule_events_file):
        with open(schedule_events_file, 'r') as file:
            data = json.load(file)
            schedule_events_obj = data
    else:
        with open(schedule_events_file, 'w') as file:
            json.dump(schedule_events_obj, file, indent=4)

    return schedule_events_obj

def check_and_schedule_events():
    while True:
        current_hour, current_minute, current_second = get_current_time()
        print(f'Current time: {current_hour}:{current_minute}:{current_second}')

        if current_second != 0:
            sleep(60 - current_second)
            continue

        schedule_events_obj = get_schedule_events()

        for schedule_event_obj in schedule_events_obj:
            for scheduling_time in schedule_event_obj['scheduling_times']:
                if int(scheduling_time['hour']) == current_hour and int(scheduling_time['minute']) == current_minute:
                    notify_event(schedule_event_obj['event_name'], schedule_event_obj['event_description'])

        sleep(60 - (time() % 60))

if __name__ == "__main__":
    check_and_schedule_events()
