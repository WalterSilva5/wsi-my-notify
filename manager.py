from PySide6.QtWidgets import (QApplication, QMainWindow, QFormLayout, QLineEdit, QPushButton, QVBoxLayout,
                               QWidget, QListWidget, QMessageBox)
import json
import os

schedule_events_file = 'schedule_events.json'

class ManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Event Scheduler Manager")
        self.setGeometry(100, 100, 500, 400)

        main_widget = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.event_name_input = QLineEdit()
        self.event_description_input = QLineEdit()
        self.hour_input = QLineEdit()
        self.minute_input = QLineEdit()

        form_layout.addRow("Event Name:", self.event_name_input)
        form_layout.addRow("Event Description:", self.event_description_input)
        form_layout.addRow("Hour (24h format):", self.hour_input)
        form_layout.addRow("Minute:", self.minute_input)

        self.add_event_button = QPushButton("Add Event")
        self.add_event_button.clicked.connect(self.add_event)

        self.add_time_button = QPushButton("Add Time to Event")
        self.add_time_button.clicked.connect(self.add_time)

        self.delete_event_button = QPushButton("Delete Selected Event")
        self.delete_event_button.clicked.connect(self.delete_event)

        self.events_list = QListWidget()
        self.events_list.itemClicked.connect(self.select_event)

        self.times_list = QListWidget()

        layout.addLayout(form_layout)
        layout.addWidget(self.add_event_button)
        layout.addWidget(self.events_list)
        layout.addWidget(self.add_time_button)
        layout.addWidget(self.times_list)
        layout.addWidget(self.delete_event_button)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        self.load_events()

    def add_event(self):
        event_name = self.event_name_input.text()
        event_description = self.event_description_input.text()

        event = {
            'event_name': event_name,
            'event_description': event_description,
            'scheduling_times': []
        }

        if os.path.exists(schedule_events_file):
            with open(schedule_events_file, 'r') as file:
                events = json.load(file)
        else:
            events = []

        events.append(event)

        with open(schedule_events_file, 'w') as file:
            json.dump(events, file)

        self.load_events()

    def add_time(self):
        selected_items = self.events_list.selectedItems()
        if not selected_items:
            return

        row = self.events_list.row(selected_items[0])
        hour = int(self.hour_input.text())
        minute = int(self.minute_input.text())

        with open(schedule_events_file, 'r') as file:
            events = json.load(file)
            events[row]['scheduling_times'].append({'hour': hour, 'minute': minute})

        with open(schedule_events_file, 'w') as file:
            json.dump(events, file)

        self.select_event(selected_items[0])

    def delete_event(self):
        selected_items = self.events_list.selectedItems()
        if not selected_items:
            return

        reply = QMessageBox.question(self, 'Delete Event', 'Are you sure you want to delete the selected event?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            row = self.events_list.row(selected_items[0])
            self.events_list.takeItem(row)

            with open(schedule_events_file, 'r') as file:
                events = json.load(file)
                del events[row]

            with open(schedule_events_file, 'w') as file:
                json.dump(events, file)

    def select_event(self, item):
        row = self.events_list.row(item)
        self.times_list.clear()

        with open(schedule_events_file, 'r') as file:
            events = json.load(file)
            times = events[row]['scheduling_times']

        for time in times:
            self.times_list.addItem(f"{time['hour']}:{time['minute']}")

    def load_events(self):
        self.events_list.clear()

        if os.path.exists(schedule_events_file):
            with open(schedule_events_file, 'r') as file:
                events = json.load(file)
                for event in events:
                    self.events_list.addItem(event['event_name'])


if __name__ == '__main__':
    app = QApplication([])
    window = ManagerWindow()
    window.show()
    app.exec_()
