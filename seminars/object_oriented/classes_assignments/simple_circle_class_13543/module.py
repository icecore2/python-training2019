class CircleData:
    # init isn't a must here
    # def __init__(self):
    def __init__(self, data):
        self.data = data

    # Area function + return added
    def area(self):
        self.r = self.data
        return 3.14 * self.r * self.r  # Area calculation
