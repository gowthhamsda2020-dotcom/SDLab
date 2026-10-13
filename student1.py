class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
student1=Student("Arun",101,85)
student1.display()