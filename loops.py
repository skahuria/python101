for i in range(0,5):
   print(i)

for i in range(20, 26):
    print(i)

# n this case, the for loop is set up so that the numbers from 0 to 15 print out,
# but at a step of 3, so that only every third number is printed
for i in range(0,15,3):
   print(i)


# Here, 100 is the start value, 0 is the stop value, and -10 is the range,
# so the loop begins at 100 and ends at 0, decreasing by 10 with each iteration
for i in range(100,0,-10):
   print(i)



sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for shark in sharks:
   print(shark)


sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for item in range(len(sharks)):
   sharks.append('shark')

print(sharks)


integers = []

for i in range(10):
   integers.append(i)

print(integers)


stephen = 'stephen'

for letter in stephen:
   print(letter)


sammy_shark = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}

for key in sammy_shark:
   print(key + ': ' + sammy_shark[key])


num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)

list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]

for list in list_of_lists:
    print(list)

list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]

for list in list_of_lists:
    for item in list:
        print(item)