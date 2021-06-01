def func1(*args):
    for i in args:
        print(i)


func1(10,20,30,40,50,60,'Zaylee','Njeri','Kimani')


def func2(**kwargs):
    for i in kwargs.items():
        print(i)


func2(a=10, b=20, c=30)

