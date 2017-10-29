import random


class Battery:
    # simulated system until we have an actual Battery #
    # system simply starts at 100 as a base, then goes slightly down, but never below 0 #

    def __init__(self):
        self.batteryLevel = 100.0

    def getBattery(self):
        self.batteryLevel = self.batteryLevel + self.randomGenerator(-1.0, 0.0)
        if self.batteryLevel < 0:
            self.batteryLevel += 1.0

        return self.batteryLevel

    def randomGenerator(self, x, y):
        randomValue = random.uniform(x, y)
        return randomValue
