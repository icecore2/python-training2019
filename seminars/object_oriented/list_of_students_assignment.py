# OOP Assignment:
# Date: Jan 2020

# Develop a separated module the includes the definition for the Student class.
# The variables each Student object should have are 'firstName', 'lastName', 'id' and 'average'.

# Develop a simple separated module (that uses the student module)
# that includes simple code for creating a list of objects.

# Each object represents a specific student in class.
# Your code should calculate the students average and print it to the screen.


class Student:
    # Methods that includes the required for the assignment:
    # firstName, lastName, id, average
    def __init__(self, firstname, lastname, id, average):
        self.firstName = firstname
        self.lastName = lastname
        self.id = id
        self.average = average
    # This method is returns the details of the student received information
    # def studentDetails(self):
    #     return "Id = %d - Name = %s %s - Average: %d" % (self.id, self.firstName, self.lastName, self.average)


class Averages(Student):
    # Initiator of the details that inherited from the 'Student' class
    def __init__(self, firstName, lastName, id, average, avg_scores):
        super().__init__(firstName, lastName, id, average)
        avg_scores = []

    def avgCalculation(self):
        average_list = []
        for avg_scores in average_list:
            average_list = [avg.average]
            return print(average_list)


# ob = Student(3423,424323,4243, 12)
# ob2 = Student(3423,424323,4243, 12)
# ob3 = Student(3423,424323,4243, 12)
# ob4 = Student(3423,424323,4243, 12)


avg = Student(3423,424323,4243, 12)
ob = Averages.avgCalculation
print(ob)


