import random


class Temperature:
    # simulated system until we have an actual thermometer #
    # system simply starts at 25 as a base, then goes slightly up or down, but never exceeding the range of 20:30 #

    def __init__(self):
        self.temp = 25.0

    def getTemp(self):
        self.temp = self.temp + self.randomGenerator(-1.0, 1.0)
        if self.temp < 20:
            self.temp += 1.0
        if self.temp > 30:
            self.temp -= 1.0

        return self.temp

    def randomGenerator(self, x, y):
        randomValue = random.uniform(x, y)
        return randomValue
