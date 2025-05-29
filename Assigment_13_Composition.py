class Engine():
    def start(self):
        print("Start Engine.....")


class Car:
    def __init__(self, engine):
        self.engine = Engine()  # 👈 Composition: Car "has an" Engine

    def start_car(self):
        print("Car is starting...")
        self.engine # 👈 Accessing Engine's method

car = Car("has")
car.start()