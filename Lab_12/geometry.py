import math

class Point:
    def __init__(self, x_axis, y_axis):
        """
        Class constructor
        :param x_axis: float
        :param y_axis: float
        """
        self.x_axis = x_axis
        self.y_axis = y_axis

    def get_distance(self):
        """
        Function that returns the distance from a point on a graph from the point of origin (0,0)
        :return: float
        """
        return f'The distance from ({self.x_axis}, {self.y_axis}) to the point of origin (0, 0) is: {round(math.sqrt((self.x_axis ** 2) + (self.y_axis ** 2)), 2)} light years.'

    def distance(self):
        """
               Function that returns the distance from a point on a graph from the point of origin (0,0) without text
               :return: float
               """
        return round(math.sqrt((self.x_axis ** 2) + (self.y_axis ** 2)), 2)

class Circle(Point):
    """
    Class extending Point class
    """
    def __init__(self, x_axis, y_axis, radius):
        super().__init__(x_axis, y_axis)
        self.radius = radius
    def get_area(self):
        return f'The area of the circle is: {round(math.pi * (self.radius ** 2), 2)} square lightyears.'

    def get_distance(self):
        return super().get_distance() - self.radius





if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(12, 8)
    print(point1.get_distance())
    print(point2.get_distance())