class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        output = []
        for s, o in zip(self.components, other.components):
            output.append(s + o)
        return tuple(output)


v1 = Vector(4, 2)
v2 = Vector(-1, 3)
print(v1 + v2)
