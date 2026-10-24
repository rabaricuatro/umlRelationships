class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name!}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def info(self):
        print(f"My name is {self.name} and my breed is a {self.breed}!"


dog = Dog("Buddy", "Golden Retriever")
dog.test()