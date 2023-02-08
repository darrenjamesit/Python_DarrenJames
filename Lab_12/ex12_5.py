from geometry import Point
import math

p1 = Point(4, 8.5)
p2 = Point(3, 4)
p3 = Point(-5, 6)
l = [p1, p2, p3]
sorted_l = sorted(l, key=Point.distance)

for i in sorted_l:
    print(f'{i.get_distance()}')