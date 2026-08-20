from abc import ABC, abstractmethod

# Abstract class
class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):

    def send(self):
        print("Notification sent through Email")

class SMSNotification(Notification):

    def send(self):
        print("Notification sent through SMS")

email = EmailNotification()
sms = SMSNotification()
email.send()
sms.send()