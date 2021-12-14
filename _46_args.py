class Vector:

    def __init__(self, *args):
        self.components = args


v1 = Vector(1, 2)
v2 = Vector(4, 5, 2)
print('v1 -> {}'.format(v1.components))
print('v2 -> {}'.format(v2.components))
