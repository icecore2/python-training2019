# OOP Assignment:
# Date: Jan 2020

# Separated module (that uses the student module)
# Simple code for creating a list of objects.
class ObjectsList:

    def objList(self, firstName, lastName, id, average):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.average = average

        testList = ObjectsList.studentList(self.firstName, self.lastName, self.id, self.average)
        print(testList)
        return testList

ObjectsList.objList("lala", "last-lala", 891238291, 23)

for testList in ObjectsList.objList:
    print(testList)

# objList = [studentDetails.Student.studentsDetails]

# for studentsDetails in objList:
#     print(studentsDetails)