from geometry import Point

x1 = float(input('Introduce the first x coordinate: '))
y1 = float(input('Introduce the first y coordinate: '))
x2 = float(input('Introduce the second x coordinate: '))
y2 = float(input('Introduce the second y coordinate: '))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

if p1.get_distance() > p2.get_distance():
    print('p1 este mai departe de centru decat p2.')
elif p2.get_distance() > p1.get_distance():
    print('p2 este mai departe de centru decat p1.')
elif p1.get_distance() == p2.get_distance():
    print('p1 și p2 sunt la aceeasi distanta fata de centru.')
else:
    print('Something went wrong...')