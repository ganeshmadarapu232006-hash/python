from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Notification):

    def send(self):
        print("Sending Email Notification")

class SMS(Notification):

    def send(self):
        print("Sending SMS Notification")

class WhatsApp(Notification):

    def send(self):
        print("Sending WhatsApp Notification")


notifications = [
    Email(),
    SMS(),
    WhatsApp()
]

for notification in notifications:
    notification.send()