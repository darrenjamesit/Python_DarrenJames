from geometry import Point, Rectangle

p1 = [-8, 10]
p2 = [4, 6]

measurements = Rectangle(p1[0], p1[1], p2[0], p2[1]).make_list()
area = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_area()
peri = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_perimetre()
print(f'Your rectangle with corners {p1}, {p2} has: \nAn area of {area} square metres \nA perimetre of {peri} metres.')
print(f'The measurements are:\nLength: {measurements[0]}\nWidth: {measurements[1]}')

if __name__ == '__main__':
    p1 = [float(input('Type the 1st x cooridnate:')), float(input('Type the 1st y cooridnate:'))]
    p2 = [float(input('Type the 2nd x cooridnate:')), float(input('Type the 2nd y cooridnate:'))]
    area = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_area()
    peri = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_perimetre()
    print(f'Your rectangle with corners {p1}, {p2} has: \nAn area of {area} square metres \nA perimetre of {peri} metres.')

