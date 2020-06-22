import pdb
from pprint import pprint
from collections import namedtuple as nt

Player = nt("Player", ["Name", "Age", "Sport"])


class Students:
    enrollment = True
    @staticmethod
    def decider(age, sport):
        if age < 18 and sport == "swimming":
            return False
        return True

    @classmethod
    def start_enrollment(cls):
        Students.enrollment = True

    @classmethod
    def stop_enrollment(cls):
        Students.enrollment = False

    def __init__(self):
        self.students = []

    def enroll_student(self, name, age, sport):
        if not Students.enrollment:
            print("Sorry Enrollments are not open, try again later")
            return
        if not self.decider(age, sport):
            print(f"Enrollment not possible in age {age} for {sport}")
            return

        self.students.append(Player(name, age, sport))

    @property
    def get_students(self):
        return self.students
        

if __name__ == "__main__":
    pdb.set_trace()
    print(f"Enroll Students")