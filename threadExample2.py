from threading import *


class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("\nThis is a child class")
            

t = MyThread()
t.start()

for i in range(5):
    print("\nThis is the main thread")