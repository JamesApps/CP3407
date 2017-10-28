class InsulinReservoir:
    # simulates the insulin reservoir attachment and needle set up
    # can either initialise under a default base 100 or have input fed in to restart pool halfway
    # needle is a simple True/False, to simulate a sensor that checks the presence of the needle assembly
    # cumulativeDose refers to the amount of insuline missing from the reservoir
    # the deliverDose function will only update the values within this object, and will not bring the insulinAvailable below 0
    # the deliverDose function will not work if the needle is removed

    def __init__(self):
        self.insulinAvailable = 100.0
        self.cumulativeDose = 0.0
        self.needle = True

    def __init(self, insulin, cumulative):
        self.insulinAvailable = insulin
        self.cumulativeDose = cumulative
        self.needle = True

    def insertNeedle(self):
        self.needle = True

    def removeNeedle(self):
        self.needle = False

    def getNeedleStatus(self):
        return self.needle

    def getInsulinAvailable(self):
        return self.insulinAvailable

    def getCumulativeDose(self):
        return self.cumulativeDose

    def deliverDose(self, dose):
        if self.needle == False:
            return
        if dose > self.insulinAvailable:
            dose = self.insulinAvailable
        self.insulinAvailable -= dose
        self.cumulativeDose += dose

    def resetReservoir(self):
        self.refillReservoir()
        self.resetCumulativeDose()

    def refillReservoir(self):
        self.insulinAvailable = 100.0

    def resetCumulativeDose(self):
        self.cumulativeDose = 0.0







