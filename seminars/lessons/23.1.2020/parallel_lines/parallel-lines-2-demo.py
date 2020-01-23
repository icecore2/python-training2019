# Define the Line and the Point classes.
# Each Line object should use two Point objects for representing a two-dimensional line.
# Develop a function that checks whether or not two lines are parallel with each other.

import math


class Point:
    # should be 2 points
    def __init__(self, firstPoint, secondPoint):
        self.x = firstPoint
        self.y = secondPoint


class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2


def parallel(l1, l2):
    # Slope calculation
    # (x1 - y1) / (x2 - y2)
    # Explained link:
    # https://lo.cet.ac.il/player/?document=ed25ea21-d22e-4848-b0ad-3e0b7c3bc1b2&language=he&sitekey=ebag#
    firstSlope =(l1.p1.x - l1.p2.x) /  (l1.p1.y - l1.p2.y)
    secondLine = (l2.p1.x - l2.p2.x) / (l2.p1.y - l2.p2.y)
    return firstSlope == secondLine


# Bulk of points to check
pnt1 = Point(2, 1)
pnt2 = Point(2, 2)
pnt3 = Point(3, 2)
pnt4 = Point(2, 1)
pnt5 = Point(5, 4)

# The lines to check
line1 = Line(pnt1, pnt2)
line2 = Line(pnt4, pnt5)

if(parallel(line1, line2)):
    print("Parallel.")
else:
    print("Not parallel.")