from geometry import Point, Circle
import math


x = float(input('Introduce the x coordinate: '))
y = float(input('Introduce the y coordinate: '))
r = float(input('Introduce the circle radius: '))

circ = Circle(x, y, r)
print(circ.get_area())
print(circ.get_distance())
