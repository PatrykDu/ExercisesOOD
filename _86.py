import uuid


class Book:

    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    def __repr__(self):
        items = [(k, v) for k, v in self.__dict__.items()]
        return "{}({}='{}', {}='{}')".format(self.__class__.__name__, items[1][0], items[1][1], items[2][0], items[2][1])

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


book1 = Book('Inferno', 'Dan Brown')
print(book1)
