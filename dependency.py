# Student temporarily uses a Printer which exists independently of Student
class Printer:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"I am a {self.brand} brand printer!")

    def printText(self, text):
        print(F"Printing: {text}")


class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am a student and my name is {self.name}!")

    def submitWork(self, printer):
        printer.printText("1 + 1 = 3")


student = Student("Alex")
printer = Printer("HP")

student.info()
printer.info()
student.submitWork(printer)