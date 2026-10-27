class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def display_details(self):
        print(f"Name:{self.name}")
        print(f"Age: {self.age}")
        print(f"Mark: {self.mark}")


Student = Student("Jhon", 20, 85)
Student.display_details()

