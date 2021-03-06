import random


class BloodGlucose:
    # simulated system until we have an actual blood sugar sensor #
    # safe values should be between 1-35 #
    # getBG() will update the blood glucose level, as well as return an alert state if it is outside normal boundaries #
    # setSafeLevels(x,y) can change the set safety levels #

    def __init__(self):
        self.bg = 10.0
        self.safeLevels = [6.0, 14.0]
        self.alert = False
        self.bgFluctuation = 1.0
        self.sensorStatus = True

# runs the update on the blood glucose using the
    def getBG(self):
        self.bg += round(self.randomGenerator(-self.bgFluctuation, self.bgFluctuation))
        if self.bg < self.safeLevels[0] or self.bg > self.safeLevels[1]:
            self.alert = True
        else:
            self.alert = False
        return self.bg

    # manually sets the safe levels for blood glucose #
    def setSafeLevels(self, safemin, safemax):
        self.safeLevels[0] = safemin
        self.safeLevels[1] = safemax

    # sets the fluctuation levels for the glucose, defaults to 2.0
    def setBGFluctuations(self, value):
        self.bgFluctuation = value

    # adds the stated value to the blood glucose levels, simulating blood glucose adjustment #
    def addBG(self, value):
        self.bg = self.bg + value

    def randomGenerator(self, x, y):
        randomValue = random.uniform(x, y)
        return randomValue
