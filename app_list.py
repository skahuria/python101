sea_creatures = ['shark', 'cuttlefish', 'squid',
                 'mantis shrimp', 'anemone']


print(sea_creatures[3] + sea_creatures[4])


# Our construction numbers[1:11:2] prints the values between index
# numbers inclusive of 1 and exclusive of 11, then the stride value of 2
# tells the program to print out only every other item.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[1:11:2])


# We can omit the first two parameters and use stride alone as a
# parameter with the syntax list[::z]:

print(numbers[::3])

# Modifying Lists with Operators

print(sea_creatures + numbers)

sea_creatures = sea_creatures + ['yeti crab']
sea_creatures += ['yeti crab']
print (sea_creatures)

print(numbers * 3)

# For each iteration of the for loop, an extra list item of 'fish' is added
# to the original list sea_creatures.
for x in range(1,4):
 sea_creatures += ['fish']
 print(sea_creatures)

sharks = ['shark']
for x in range(1,4):
 sharks *= 2
 print(sharks)

# Removing an Item from a List

sea_creatures =['shark', 'octopus', 'blobfish',
'mantis shrimp', 'anemone', 'yeti crab']
del sea_creatures[1]
print(sea_creatures)

# By using a range with the del statement, we were able to remove the
# items between the index number of 1 (inclusive), and the index number
# of 4 (exclusive), leaving us with a list of 3 items following the removal of
# 3 items.
sea_creatures =['shark', 'octopus', 'blobfish',
'mantis shrimp', 'anemone', 'yeti crab']
del sea_creatures[1:4]
print(sea_creatures)

# Constructing a List with List Items
# Lists can be defined with items that are made up of lists, with each
# bracketed list enclosed inside the larger brackets of the parent list
# sea_names[0][0] = 'shark'
# sea_names[0][1] = 'octopus'
# sea_names[0][2] = 'squid'
# sea_names[0][3] = 'mantis shrimp'
# sea_names[1][0] = 'Sammy'
# sea_names[1][1] = 'Jesse'
# sea_names[1][2] = 'Drew'
# sea_names[1][3] = 'Jamie'

sea_names = [['shark', 'octopus', 'squid', 'mantis shrimp'],
             ['Sammy', 'Jesse', 'Drew', 'Jamie']]

print(sea_names[1][0])
print(sea_names[0][0])

