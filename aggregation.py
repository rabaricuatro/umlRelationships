#$ Classroom has a Student which can exist independently of Classroom
class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am a student and my name is {self.name}!")


class Classroom:
    def __init__(self, student):
        self.student = student

    def info(self):
        print("Classroom information:")
        self.student.info()


student = Student("Alex")
classroom = Classroom(student)
classroom.info()
