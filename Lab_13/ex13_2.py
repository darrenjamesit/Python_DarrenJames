class Rectangle_abs:
    """
    New class without using abs
    """
    def __init__(self, x_axis, y_axis, x_axis2, y_axis2):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_axis2 = x_axis2
        self.y_axis2 = y_axis2
        """
        Constructor for class rectangle
        :param x_axis: 
        :type: float
        :param y_axis: float
        :param x_axis2: float
        :param y_axis2: float
        """

    def make_list(self):
        """
        Makes a list of the legnth and width of a rectangle for later use
        :returns: list
        """
        lth = self.x_axis - self.x_axis2
        if lth < 0:
            length = lth * (-1)
        else:
            length = lth
        wth = self.y_axis - self.y_axis2
        if wth < 0:
            width = wth * (-1)
        else:
            width = wth
        values = [length, width]
        return values

    def get_area(self):
        """
        Calculates area of rectangle.
        :returns: int
        """
        rez = Rectangle_abs.make_list(self)
        area = rez[0] * rez[1]
        if area:
            return area
        else:
            return 'This is not a rectangle.'

    def get_perimetre(self):
        """
        Calculates the perimetre of a rectangle.
        :returns: int
        """
        result = Rectangle_abs.make_list(self)
        peri = 2 * (result[0] + result[1])
        if peri:
            return peri

p1 = [-8, 10]
p2 = [4, 6]
measurements = Rectangle_abs(p1[0], p1[1], p2[0], p2[1]).make_list()

area = Rectangle_abs(p1[0], p1[1], p2[0], p2[1]).get_area()
peri = Rectangle_abs(p1[0], p1[1], p2[0], p2[1]).get_perimetre()
print(f'Your rectangle with corners {p1}, {p2} has: \nAn area of {area} square metres \nA perimetre of {peri} metres.')
print(f'The measurements are:\nLength: {measurements[0]}\nWidth: {measurements[1]}')
