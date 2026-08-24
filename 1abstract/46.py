from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)

class OnlineCourse(Course):

    def start(self):
        print("Online course started")

class OfflineCourse(Course):

    def start(self):
        print("Offline course started")

online = OnlineCourse("Python Programming", "3 Months")
offline = OfflineCourse("Web Development", "6 Months")

online.display_course_details()
online.start()
offline.display_course_details()
offline.start()