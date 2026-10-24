# Cat implements info method from Animal
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def info(self):
        pass


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am a cat named {self.name}. Meow!")


cat = Cat("Meeow")
cat.info()
