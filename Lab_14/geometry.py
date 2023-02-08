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

    def __str__(self):
        return f'Point({self.x_axis}, {self.y_axis})'

    def distance(self):
        """
               Function that returns the distance from a point on a graph from the point of origin (0,0) without text
               :return: float
               """
        return round(math.sqrt((self.x_axis ** 2) + (self.y_axis ** 2)), 2)

    def lis(self):
        return f'Point{(self.x_axis, self.y_axis)}'


class Circle(Point):
    """
    Class extending Point class
    """
    def __init__(self, x_axis, y_axis, radius):
        super().__init__(x_axis, y_axis)
        self.radius = radius
    def get_area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def get_distance(self):
        return super().get_distance() - self.radius


class Rectangle:
    """
    Rectangle class
    """
    instances = 0
    square_instances = 0


    def __init__(self, x_axis : Point, y_axis : Point, x_axis2 : Point, y_axis2 : Point):
        """
               Constructor for class rectangle

               """
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_axis2 = x_axis2
        self.y_axis2 = y_axis2
        Rectangle.instances += 1

    def __str__(self):
        return f"Rectangle(Point{self.x_axis}, {self.y_axis}), Point({self.x_axis2}, {self.y_axis2}"

    def make_list(self):
        """
        Makes a list of the length and width of a rectangle for later use
        :returns: list
        """
        length = abs(self.x_axis - self.x_axis2)
        width = abs(self.y_axis - self.y_axis2)
        values = [length, width]
        return values

    def get_area(self):
        """
        Calculates area of rectangle.
        :returns: int
        """
        rez = self.make_list()
        area = rez[0] * rez[1]
        return area


    def get_perimetre(self):
        """
        Calculates the perimetre of a rectangle.
        :returns: int
        """
        result = Rectangle.make_list(self)
        peri = 2 * (result[0] + result[1])
        if peri:
            return peri

    def isin_rectangle(self, new_point_x, new_point_y):
        """
        Checks if point is inside rectangle
        :returns: True/False
        """
        self.new_point_x = new_point_x
        self.new_point_y = new_point_y
        if self.x_axis <= self.new_point_x <= self.x_axis2 or self.x_axis >= self.new_point_x >= self.x_axis2:
            if self.y_axis <= self.new_point_y <= self.y_axis2 or self.y_axis >= self.new_point_y >= self.y_axis2:
                return True
        else:
            return False

    def circ_isinrectangle(circ, new_point_x, new_point_y, radius):
        """
        Checks if circle is in the defined rectangle
        :returns: True/False
        """
        circ.new_point_x = new_point_x
        circ.new_point_y = new_point_y
        rectangle_centre_x = (circ.x_axis + circ.x_axis2) / 2
        rectangle_centre_y = (circ.y_axis + circ.y_axis2) / 2

        #distance formula:

        dist = math.sqrt((circ.new_point_x - rectangle_centre_x) ** 2 + (circ.new_point_y - rectangle_centre_y) ** 2)

        return dist < radius


    def __eq__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        sort_r1 = sorted(r1)
        sort_r2 = sorted(r2)
        return sort_r1 == sort_r2

    def is_square(self):
        if self.make_list()[0] == self.make_list()[1]:
            Rectangle.square_instances += 1
        return self.make_list()[0] == self.make_list()[1]

    @staticmethod
    def show_instances():
        return f'There is/are {Rectangle.instances} class instances so far..\nand there is/are {Rectangle.square_instances} square instances so far..'

    def get_square_percent(self):
        return f'Squares make up {Rectangle.square_instances / Rectangle.instances * 100}% of all instances.'


class Polyline:
    def __init__(self, *args):
        self.args = args
        if type(args) is not tuple:
            raise WrongGeometry("The provided object needs to be class Point")

        if len(args) < 2:
            raise min2("Needs to be at least 2 long")

    def __str__(self):
        return f'Polyline{self.args}'


class  WrongGeometry(TypeError):
    pass

class min2(Exception):
    pass

if __name__ == '__main__':
    p1 = [float(input('Type the 1st x cooridnate:')), float(input('Type the 1st y cooridnate:'))]
    p2 = [float(input('Type the 2nd x cooridnate:')), float(input('Type the 2nd y cooridnate:'))]
    area = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_area()
    peri = Rectangle(p1[0], p1[1], p2[0], p2[1]).get_perimetre()
    print(f'Your rectangle with corners {p1}, {p2} has: \nAn area of {area} square metres \nA perimetre of {peri} metres.')

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(12, 8)
    print(p1.get_distance())
    print(p2.get_distance())
