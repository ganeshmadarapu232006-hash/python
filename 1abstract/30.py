from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def display_details(self):
        pass

class OnlineCourse(Course):

    def display_details(self):
        print("Online Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)

class OfflineCourse(Course):

    def display_details(self):
        print("Offline Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)

online = OnlineCourse("Python Programming", "3 Months")
offline = OfflineCourse("Web Development", "6 Months")


online.display_details()

print()

offline.display_details()