class Dog:
    def __init__(self, name: str, breed:str):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name}.")

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()