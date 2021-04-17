def square(x):
    y = x ** 2
    return y


result = square(3)
print(result)




def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    return a, b, c


sums = add_numbers(1, 2, 3)
print(sums)