from geometry import Rectangle

p1 = Rectangle(1, 1, 2, 2).is_square()
p2 = Rectangle(11, 21, 32, 24).is_square()
p3 = Rectangle(4, 7, 9, 9).is_square()
p4 = Rectangle(10, 1, 2, 20).is_square()

print(p1)
print(p2)
print(p3)
print(p4)
print(Rectangle.show_instances())
print(Rectangle.get_square_percent())