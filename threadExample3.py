from threading import *


class Demo:
    def show(self):
        for i in range(5):
            print("This is the child thread")


obj = Demo()
t = Thread(target=obj.show())
t.start()
for i in range(5):
    print("This is the parent thread")