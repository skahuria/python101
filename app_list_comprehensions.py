shark_letters = [letter for letter in 'Stephen']
print(shark_letters)


shark_letters = []
for letter in 'Stephen':
  shark_letters.append(letter)

print(shark_letters)


fish_tuple = ('blowfish', 'clownfish', 'catfish',
'octopus')
fish_list = [fish for fish in fish_tuple if fish !=
'octopus']
print(fish_list)

# The list that is being created, number_list, will be populated with
# the squared values of each item in the range from 0-9 if the item’s value is
# divisible by 2.
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)


number_list = [x for x in range(10)]
print(number_list)

# Here, the list comprehension will first check to see if the number x is
# divisible by 3, and then check to see if x is divisible by 5. If x satisfies
# both requirements it will print

number_list = [x for x in range(100)]
print(number_list)

number_list = [x for x in range(100) if x % 3 == 0 if
x % 5 == 0]
print(number_list)

my_list = []
for x in [20, 40, 60]:
  for y in [2, 4, 6]:
    my_list.append(x * y)
print(my_list)


my_list = [x * y for x in [20, 40, 60]for y in [2, 4,6]]
print(my_list)