""" OOP Assignment:
# Date: Jan 2020
Link: http://lifemichael.com/moodle/mod/assign/view.php?id=13545

Develop a separated module the includes the definition for the Student class.
The variables each Student object should have are 'firstName', 'lastName', 'id' and 'average'.
Develop a simple separated module (that uses the student module)
that includes simple code for creating a list of objects.
Each object represents a specific student in class.
Your code should calculate the students average and print it to the screen.
"""


class Student:
    def __init__(self, sid, fname, lname, avg):
        self.__sid = sid
        self.__fname = fname
        self.__lname = lname
        self.__avg = avg

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def sid(self, value):
        self.__sid = value

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, value):
        self.__fname = value

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, value):
        self.__lname = value

    @property
    def avg(self):
        return self.__avg

    @avg.setter
    def avg(self, value):
        if 100 >= value >= 0:
            self.__avg = value


# List of students with: id, first name, last name, average score
students = [
    Student(124, "mosh", "levy", 80),
    Student(12284, "mos2h", "lkaslasvy", 97),
    Student(122384, "mos21h", "sad", 95),
    Student(112284, "mo1s2h", "gea", 91),
    Student(122284, "mos32h", "fasd", 92)
]

# Define new variable with a default value
total = 0

# Create a loop for adding the average scores
for student in students:
    total += student.avg

# New variable to get the number of the scores
number = len(students)

''' The result includes:
    1. result of the total (number of all scores together)
    2. number of a students (to devide by this)
    3. Save to variable
'''
result = total / number

print(result)
# print(student)
