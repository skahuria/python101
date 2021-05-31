class car():

    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getspeed(self):
        print("Maximum speed is: ", self.speed)


BMW = car(2018,155)
FORD = car(2016, 140)

car.getspeed(BMW)
car.getspeed(FORD)

# or

BMW.getspeed()
FORD.getspeed()