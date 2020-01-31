# PDF - Page 13

# Person() class is the initiator of the variables
class Person:
    # Initiator of the variables
    def __init__(self, id, name, lname):
        self.id = id
        self.firstName = name
        self.lastName = lname

    # Details return function
    def details(self):
        return "Id = %d - Name = %s %s" % (self.id, self.firstName, self.lastName)


# Student is inherited the Person() class for the variables
class Student(Person):
    def __init__(self, id, firstName, lastName, average):
        self.average = average
        super().__init__(id, firstName, lastName)

    def details(self):
        return super().details() + " average=%d" % self.average


ob = Student(123123, "danidin", "babani", 98)
print(ob.details())
