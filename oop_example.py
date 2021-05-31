class car():

    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getspeed(self):
        print("Maximum speed is: ", self.speed)

    def setSpeed(self, speed):
        self.speed = speed


BMW = car(2018,155)
FORD = car(2016, 140)

class Sedan(car): # child class
    def accelerate(self):
        print('137')
    def openTrunk(self):
            print('trunk has been opened')

class SUV(car): # child class
    def accelerate(self):
        print('127')

BMW.getspeed()
BMW.setSpeed(143)
BMW.getspeed()
FORD.getspeed()
Honda= Sedan(2018,150)
Honda.getspeed()
Honda.openTrunk()
