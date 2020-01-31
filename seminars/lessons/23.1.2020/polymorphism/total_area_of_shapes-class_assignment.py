# You should define the Shape class. The Shape class should include one method only. The printDetails() method.
# Calling this method we shall get, printed to the screen, the text "i am a Shape" together with the area.

# You should define two classes that extend Shape. The first is Circle. The second is Rectangle.
# Both the class Circle and Rectangle should include the definition for the area() method.

# Each object instantiated from Circle should include the radius attribute.
# The Circle __init__ method should receive the radius of the new created object.

# Each object instantiated from Rectangle should include the width and height attributes.
# The Rectangle __init__ method should receive the width and the height of the new created object.

# You should use the classes you defined for creating a list of objects that represent the
# following shapes and calculate the total area of all shapes:
# 1. circle, radius=5
# 2. rectangle, width=7, height=9
# 3. rectangle, width=6, height=10
# 4. circle, radius=8

import math


class Shape:
    # init isn't a must here
    # def __init__(self):
    def printDetails(self):
        print("I am a Shape.", self.area())


class Cicle(Shape):
    def __init__(self, radius):
        self.r = radius

    # Area function + return added
    def area(self):
        # piNumber = math.pi.real.as_integer_ratio()
        return 3.14 * self.r * self.r  # Area calculation


class Rectangle(Shape):
    def __init__(self, width, height):
        self.w = width
        self.h = height
    # added
    def area(self):
        return self.w * self.h

# Data of the shapes
shapes = [Cicle(5),
          Cicle(8),
          Rectangle(7, 8),
          Rectangle(6, 10)]

total = 0

for shape in shapes:
    total = total + shape.area()

print(total.real)

