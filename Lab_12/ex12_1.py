import math
import time

class Point:
    def __init__(self, x_axis, y_axis):
        """
        Class constructor
        :param x_axis: coordinate X
        :type x: float

        :param y_axis: float
        """
        self.x_axis = x_axis
        self.y_axis = y_axis

    def get_distance(self):
        """
        Function that returns the distance from a point on a graph from the point of origin (0,0)
        :returns: distanta...
        :rtype: float
        """
        return f'The distance from ({self.x_axis}, {self.y_axis}) to the point of origin (0, 0) is: {round(math.sqrt((self.x_axis ** 2) + (self.y_axis ** 2)), 2)} light years.'

start = time.process_time_ns()
# actual time at the start of program (in nanoseconds)

x = float(input('Introdu valoarea coordonatei x: '))
y = float(input('Introdu valoarea coordonatei y: '))

point1 = Point(x, y)
print(point1.get_distance())

end = time.process_time_ns()
# actual time at the end of program (in nanoseconds)

final_time = end - start

print(f'Total process time: {final_time/1000000} milliseconds')