# Define the Line and the Point classes.
# Each Line object should use two Point objects for representing a two-dimensional line.
# Develop a function that checks whether or not two lines are parallel with each other.

class Point:
    # should be 2 points
    def pointA(self, firstPoint):
        self.firstPoint = firstPoint
        return self.firstPoint

    def pointB(self, secondPoint):
        self.secondPoint = secondPoint
        return self.secondPoint


class Line:
    point = Point()
    point.pointA(1)
    point.pointB(1)

    if point.firstPoint == point.secondPoint:
        print("This equals.")
    else:
        print("The points doesn't at the same place.")

