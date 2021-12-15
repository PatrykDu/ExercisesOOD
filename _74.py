import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self._area = None
        # self._area = math.pi * (radius * radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        self._area = math.pi * (self.radius * self.radius)
        return self._area


circle = Circle(3)
print(round(circle.area, 4))
