class Car:
    def __init__(self,brand: str ):
        self.brand: str = brand
        
    def start(self):
        print(f"My {self.brand} car is starting.")



car1 = Car("Toyota")
print(car1.brand)
car1.start()
