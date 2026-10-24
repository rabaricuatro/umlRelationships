# Engine is a part of Car; Car creates instance of Engine
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def info(self):
        print(f"I have {self.horsepower} horsepower!")


class Car:
    def __init__(self, horsepower):
        self.engine = Engine(horsepower)

    def info(self):
        print("Car information:")
        self.engine.info()


car = Car(150)
car.info()