from datetime import date
import datetime

# Introduction
print("Stephen Kahuria")
print('o----')
print(' |||| ')
print('*' * 10)


# How to define Variables
price = 10
price = 20
rating = 4.9
name = 'Stephen'
is_published = False
print(price)
print(is_published)
print(rating)

# We check in a patient named John Smith. He's 20 years old an is a new patient
name = 'John Smith'
age = 20
is_newPatient = True

# Receive input from user
name = input('What is your name ? ')
color = input('What is your favourite color? ')
print(name + ' likes '+ color)

# Type Conversion- Calculate birthday
birth_year = input('Birth year: ')
print(type(birth_year))
age = datetime.datetime.now().year - int(birth_year)
print(type(age))
print('Your age is', age)

# Ask a user their weight(in pounds), convert it to
# Kilograms and print on the terminal
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# Strings
course = 'Python for "Beginners"'
email = ''' 
Hi Stephen,

Here is our first email to you.

Thank you,
The support team
 '''
another = course[:]
name = 'Stephen'
print(course)
print(email)
print(course[0])
print(course[-1])
print(course[0:3])
print(another)
print(name[1:-1])

# Formatted Strings
first = 'Stephen'
last = 'Kahuria'
msg = f'{first} {last} is a coder'
print(msg)

# String Methods

website = 'Stephen Kahuria'
print(len(website))
print(website.upper())
print(website.find('S'))
print(website.replace('Stephen', 'Zaylee'))
print('Stephen' in website)

# Arithmetic Operations
# Order of Operations
# parenthesis, exponentiation, multiplication, division, addition, subtraction

x = 10
x = x +3
x += 3
x -=3
x = 10 + 3 * 2

#Math Functions
import math
x = 2.9
print(abs(-2.9))
print(math.floor(2.9))
print(math.ceil(2.9))

# If Statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Price of a house is $1M
# If buyer has good credit,
#    they need to put down 10%
# Otherwise
#    they need to put down 20%

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# Logical Operators

# If applicant has high income
# AND good credit
# Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# If name is less than 3 characters long
#      name must be at least 3 characters
# Otherwise it its more than 50 characters long
#   name can be a maximum of 50 characters
# Otherwise
#   name looks good
name = "J"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Weight Converter
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pound")

# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# Guessing Game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
else: print('Sorry you failed!')

# Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
        print("Car started..")
    elif command == "stop":
        if not started:
            print("Car is already stopped ")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")

# For Loops

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
    print(f"Total: {total}")

# Nested Loops

for x in range(4):
    for y in range(3):
        print(f' ({x}, {y})')


numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# Lists
# Find Largest Number in a list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# List Methods

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
number.append(10)
numbers.sort()
numbers.reverse()
print(numbers)

# Remove duplicates in a list

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Tuples
# Cannot be changed

# Unpacking

coordinates = (1, 2 , 3)
x , y, z = coordinates

# Dictionaries

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))

# Translate

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

####
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


























































































