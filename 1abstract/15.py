from abc import ABC, abstractmethod

# Abstract class
class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass


# Email class
class Email(Notification):

    def send(self):
        print("Email notification sent")

    def schedule(self):
        print("Email notification scheduled")


# SMS class
class SMS(Notification):

    def send(self):
        print("SMS notification sent")

    def schedule(self):
        print("SMS notification scheduled")


# WhatsApp class
class WhatsApp(Notification):

    def send(self):
        print("WhatsApp notification sent")

    def schedule(self):
        print("WhatsApp notification scheduled")


# Creating objects
email = Email()
sms = SMS()
whatsapp = WhatsApp()

# Calling methods
email.send()
email.schedule()

sms.send()
sms.schedule()

whatsapp.send()
whatsapp.schedule()