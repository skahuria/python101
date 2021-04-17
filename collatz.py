def collatz(number):
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
        elif number % 2 == 1:
            print(number * 3 + 1)
            number =  number *3 + 1

try:
    print ('Enter the number to Collatz:')
    collatz(int(input()))
except ValueError:
    print('Enter a valid integer')
