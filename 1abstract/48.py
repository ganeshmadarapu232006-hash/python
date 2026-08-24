from abc import ABC, abstractmethod

class Notification(ABC):

    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message:", self.message)

class Email(Notification):

    def send(self):
        print("Message sent through Email")

class SMS(Notification):

    def send(self):
        print("Message sent through SMS")

class WhatsApp(Notification):

    def send(self):
        print("Message sent through WhatsApp")

email = Email("Hello, how are you?")
sms = SMS("Your OTP is 1234")
whatsapp = WhatsApp("Meeting at 10 AM")
email.display_message()
email.send()
sms.display_message()
sms.send()
whatsapp.display_message()
whatsapp.send()