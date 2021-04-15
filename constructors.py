# Constructor
# Gets called at the time of creating an object
class Point:
     def __init__(self, x, y):
         self.x = x
         self.y = y

     def move(self):
         print("move")

     def draw(self):
         print("draw")


# Create Objects
point = Point(10, 20)
print(point.x, point.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


stephen = Person("Stephen Kahuria")
stephen.talk()

zaylee = Person("Zaylee Njeri")
zaylee.talk()



