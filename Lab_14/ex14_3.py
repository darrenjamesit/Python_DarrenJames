from geometry import Point, Polyline

p1 = Point(3, 4).lis()
p2 = Point(4, 5).lis()
p3 = Point(5, 6).lis()
p4 = Point(16, 9).lis()


poly = str(Polyline(p1, p2, p3, p4)).replace("'", "")

print(poly)