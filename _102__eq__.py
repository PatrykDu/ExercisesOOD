class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __eq__(self, other):
        if self.string == other.string:
            return True
        else:
            return False


doc1 = 'Python'
doc2 = '3.8'

print(doc1 == doc2)
