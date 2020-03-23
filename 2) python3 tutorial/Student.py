
from Human import Human

class Student(Human):

    count = 0
    def __init__(self, name, age, height, weight, stdID, uni, field):
        super().__init__(name, age, height, weight)
        self.stdID = stdID
        self.uni = uni
        self.field = field
        Student.count += 1

    def get_info_student(self):

        return f'The Name is {self.name}, SudentID: {str(self.stdID)} , university: {self.uni}, Field: {self.field}'

milad = Student('milad',25,170,70,stdID=97464120,uni='zanjan',field='Software enginner')
print(milad.get_info_student())
print("Student Count: ", Student.count)
