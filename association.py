# Teacher and Student are associated, but exist independently of one another
class Teacher:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am a teacher and my name is {self.name}!")


class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def info(self):
        print(f"I am a student named {self.name} and my teacher is {self.teacher.name}!")


teacher = Teacher("Ms. Baker")
student = Student("Alex", teacher)

teacher.info()
student.info()