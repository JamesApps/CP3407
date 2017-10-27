import datetime
import time

class Clock:

    def __init__(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        self.printTime()

    def setClock(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def printTime(self):
        print("Current time is "+str(self.hours)+" hours, "+str(self.minutes)+" minutes, and "+str(self.seconds)+" seconds.")

    def tickUp(self):
        while True:
            time.sleep(1)
            self.seconds += 1
            if self.seconds > 59:
                self.seconds = 0
                self.minutes += 1
            if self.minutes > 59:
                self.minutes = 0
                self.hours += 1
            if self.hours > 23:
                self.hours = 0
            break

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def getTime(self):
        #returns time as a list#
        time = [self.hours, self.minutes, self.seconds]
        return time

    def setLocalTime(self):
        localtime = datetime.datetime.now()
        self.hours=localtime.hour
        self.minutes=localtime.minute
        self.seconds=localtime.second


