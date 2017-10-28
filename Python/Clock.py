import datetime
import time


class Clock:

    def __init__(self, hour, minute, second):
        # initialisation using set time #
        self.hours = hour
        self.minutes = minute
        self.seconds = second
        self.printTime()

    def __init__(self):
        # initialisation defaults to using local time #
        self.setLocalTime()
        self.printTime()

    def setClock(self, hour, minute, second):
        # setting method #
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def printTime(self):
        print("Current time is {:02}:{:02}:{:02}" .format(self.hours, self.minutes, self.seconds))

    def tickUp(self):
        # when called, waits one second, then ticks the seconds up by one #
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
        # returns time as a list #
        time = [self.hours, self.minutes, self.seconds]
        return time

    def setLocalTime(self):
        # sets clock timing to local time #
        localtime = datetime.datetime.now()
        self.hours = localtime.hour
        self.minutes = localtime.minute
        self.seconds = localtime.second
