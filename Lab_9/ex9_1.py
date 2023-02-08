from math import *

l = [(5, 21), (6, 11), (0, 25), (-6, 6)]

sort_l = sorted(l, key=lambda x: prod(x))

print(sort_l)
