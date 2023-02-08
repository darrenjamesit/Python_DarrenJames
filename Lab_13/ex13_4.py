from geometry import Point, Circle, Rectangle

p1 = [float(input('Type the 1st x cooridnate: ')), float(input('Type the 1st y cooridnate: '))]
p2 = [float(input('Type the 2nd x cooridnate: ')), float(input('Type the 2nd y cooridnate: '))]
new_x = float(input('Type x value of circle to check if in rectangle: '))
new_y = float(input('Type y value of circle to check if in rectangle: '))
r = float(input('Type radius of circle: '))

resul = Rectangle(p1[0], p1[1], p2[0], p2[1]).circ_isinrectangle(new_x, new_y, r)

print(resul)