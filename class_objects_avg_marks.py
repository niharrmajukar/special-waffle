
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for mark in self.marks:
            total += mark

        print("Hi", self.name, "your average score is:", total / len(self.marks))



s1 = Student(input("please enter your namer: "), [90, 80, 70])
s1.get_avg()