from geometry import Point

x = float(input('Introdu valoarea coordonatei x: '))
y = float(input('Introdu valoarea coordonatei y: '))

ex_point = Point(x, y)
print(ex_point.get_distance())
