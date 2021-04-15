# Functions
def greet_user():
    print('Hi there ! Welcome aboard')


print("Start")
greet_user()
print("Finish")


# Parameters
# Positional Arguments
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}! Welcome aboard')


print("Start")
greet_user("Stephen", "Kahuria")
greet_user("Zaylee", "Njeri")
print("Finish")


# Keyword Arguments
# Come after Positional Arguments
# Position does not matter
# Numerical

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}! Welcome aboard')


print("Start")
greet_user(first_name="Stephen",last_name= "Kahuria")
greet_user(first_name="Zaylee", last_name="Njeri")
print("Finish")


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}! Welcome aboard')


print("Start")
greet_user("Stephen",last_name= "Kahuria")
greet_user("Zaylee", last_name="Njeri")
print("Finish")


# Return Statement
def square(number):
    return number * number


print(square(3))

# Reusable Function

# def emoji_converter(message):
#     words = message.split("")
#     emojis = {
#         ":)": " ",
#         ":(": " "
#     }
#     output = ""
#     for word in words:
#         output +=emojis.get(word, word) + " "
#         return output
#      print(output)

# Exceptions
try:
    age = int(input('Age: '))
    print(age)
    income = 20000
    risk = income / age

except ZeroDivisionError:
    print('Age cannot be 0.')

except ValueError:
    print('Invalid value')


























