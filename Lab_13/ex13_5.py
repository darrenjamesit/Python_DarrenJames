from geometry import Point, Rectangle

x1 = float(input('Type the 1st x cooridnate: '))
y1 = float(input('Type the 1st y cooridnate: '))
x2 = float(input('Type the 2nd x cooridnate: '))
y2 = float(input('Type the 2nd x cooridnate: '))

rect_1 = Rectangle(x1, y1, x2, y2).make_list()

x3 = float(input('Type the 3rd x cooridnate: '))
y3 = float(input('Type the 3rd y cooridnate: '))
x4 = float(input('Type the 4th x cooridnate: '))
y4 = float(input('Type the 4th x cooridnate: '))

rect_2 = Rectangle(x3, y3, x4, y4).make_list()
print(rect_1, rect_2)

#Using '==' operator

print(rect_1 == rect_2)

#Using operator overloading
rez = Rectangle(x1, y1, x2, y2).__eq__(rect_1, rect_2)

print(rez)
