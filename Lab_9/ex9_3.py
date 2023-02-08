l_1 = [2, 3, 1]
l_2 = [1, 4, 5]
l_3 = ['A', 'q', '#']

map_madness = list(map(lambda x, y, z: (x + y) * z, l_1, l_2, l_3))

print(map_madness)
