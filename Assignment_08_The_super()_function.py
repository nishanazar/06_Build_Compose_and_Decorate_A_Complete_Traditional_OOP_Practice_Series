class Person:
    def __init__(self, name: str):
        self.name: str = name



class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject: str = subject


person = Person("Ali")
print(person.name)

teacher = Teacher("Hashir", "English")
print(teacher.name)
print(teacher.subject)

    
        