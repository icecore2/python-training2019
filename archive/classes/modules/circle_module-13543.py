import math


class Circle:
    ''' This is a circle class that includes required functions.

        :param r = Radius
    '''
    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)
