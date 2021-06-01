def func1(called_func):
    print("This is the first function")

    def nested_func1(called_func):
        print("This is the nested function")
        called_func()
    return nested_func1(called_func)


def outer_func():
    print("This is the outer function")


obj = func1(outer_func)