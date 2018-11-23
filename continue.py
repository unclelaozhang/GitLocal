players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions =(400,100)
print('Modified dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions =(200, [20,100])
for dimension in dimensions:
    print(dimension)
dimension[1][0] = [10]
