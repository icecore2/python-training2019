"""
Link: http://lifemichael.com/moodle/mod/assign/view.php?id=13543

Develop a simple module that includes the definition for the Circle class.
Each object instantiated from that class should represent a specific circle.
The definition for the Circle class should include two methods:
    * area()
    * perimeter().

Develop a separated module that uses the circle module and creates two objects for representing two circles.
* The first circle has the 5cm radius.
* The second circle has the 6cm radius.

Your code should print out the area and the perimeter of each one of these two circles.

What I need:
1. Module (CircleData())
    * Circle methods:
        1. def area()
        2. def perimeter()
2. Module 2 (Circle())
    * Uses the first Module to create a 2 objects
        1. circle 1 = 5cm radius
        2. circle 2 = 6cm radius
    * print the perimeter()
"""
from seminars.object_oriented.classes_assignments.simple_circle_class_13543.module import CircleData


class Circle(CircleData):
    def print_details(self):
        print("I am a Shape.", self.area())


""" 
This is variables for filing out the class parameters
You can see here that the 2 classes is related to each other by this example:
x = CircleData(5)
y = Circle(5)
"""

x = Circle(5)
y = Circle(6)
print("Printing the variables: \nx =", x.area(), "\ny =", y.area())
