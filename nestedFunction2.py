def func1(called_func):
    print("This is the first function")

    def nested_func1():
        print("This is the nested function")
        called_func()
    return nested_func1

@func1
def outer_func():
    print("This is the outer function")


outer_func()