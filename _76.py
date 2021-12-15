class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        return self._height

    @property
    def area(self):
        self._area = self.width * self.height
        return self._area


rectangle = Rectangle(3, 4)
print('width: {}, height: {} -> area: {}'.format(rectangle.width, rectangle.height, rectangle.area))
