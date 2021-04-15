# Classes

class Point:
    # methods
     def move(self):
         print("move")

     def draw(self):
         print("draw")


# Create Objects
point1 = Point()
point1.draw()
point1.move()

# attributes
point1.x = 20
point1.y = 10
print(point1.x,",",point1.y)
point1.draw()

point2 = Point()
point2.x = 30
print(point2.x)
