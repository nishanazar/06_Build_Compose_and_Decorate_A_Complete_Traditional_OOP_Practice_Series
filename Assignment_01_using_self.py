 #------------ Task 1: Using `self`-----------------

class Student:
    def __init__(self, name:str , marks:int):
        self.name: str = name
        self.marks: int = marks

    def display(self)->None:
        print(f"My name is {self.name} and my marks are {self.marks}.")



student_01: Student = Student("ali", 550)
student_01.display()



