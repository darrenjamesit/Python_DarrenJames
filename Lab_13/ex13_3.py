from geometry import Point, Rectangle

p1 = [float(input('Type the 1st x cooridnate: ')), float(input('Type the 1st y cooridnate: '))]
p2 = [float(input('Type the 2nd x cooridnate: ')), float(input('Type the 2nd y cooridnate: '))]
new_x = float(input('Type x value to check if in rectangle: '))
new_y = float(input('Type y value to check if in rectangle: '))


res = Rectangle(p1[0], p1[1], p2[0], p2[1]).isin_rectangle(new_x, new_y)

print(res)

#eg True p1 (2, 4), p2 (5, 9), new x new y (3, 5)
#eg False p1 (2, 4), p2 (5, 9), new x new y (1, 1)