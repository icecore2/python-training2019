"""
Link: http://lifemichael.com/moodle/mod/assign/view.php?id=13544

Develop a simple module that includes the definition for the Rectangle class.
Each object instantiated from that class should represent a specific rectangle.
The definition for the Rectangle class should include two methods:
    1. area()
    2. perimeter().

Develop a separated module that uses the rectangle module and creates two objects for representing two rectangles.
The first rectangle has the 5cm width and 8cm height.
The second rectangle has the 6cm width and 9cm height.

Your code should print out the area and the perimeter of each one of these two rectangles.

"""

from seminars.object_oriented.classes_assignments.simple_rectangle_class_13544.module import RectangleData


class Rectangle(RectangleData):
    def print_details(self):
        print("I am a Shape.", self.area())


# Works also:
# ob = Rectangle(6, 6).print_details()

# Parameters fill and printing
ob = Rectangle(6, 6)
print("print: ", ob.area())
