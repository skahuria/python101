import random

for i in range(7):
    print(random.randint(10, 20))


for i in range(6):
    print(random.randint(20, 30))


members = ['Stephen', 'Zaylee', 'Ann', 'Helen', 'Simon', 'Peter', 'James', 'Andrew']
leader = random.choice(members)
print(leader)


