fish = ['barracuda','cod','devil ray','eel']


fish.append('flounder')
print(fish)

fish.insert(0,'anchovy')
print(fish)

fish.insert(3,'damselfish')
print(fish)

more_fish = ['goby','herring','ide','kissing gourami']
fish.extend(more_fish)
print(fish)

fish.remove('kissing gourami')
print(fish)

print(fish.pop(3))
print(fish)

print(fish)
print(fish.index('herring'))

fish_2 = fish.copy()
print(fish_2)

fish.reverse()
print(fish)

print(fish.count('goby'))

fish_ages = [1,2,4,3,2,1,1,2]
print(fish_ages.count(1))

fish_ages.sort()
print(fish_ages)

fish.clear()
print(fish)