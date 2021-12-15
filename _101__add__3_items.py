class Hashtag:

    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)


h1 = Hashtag('python')
h2 = Hashtag('developer')
h3 = Hashtag('oop')

print(h1 + h2 + h3)
