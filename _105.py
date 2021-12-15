import uuid


class Book:

    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    def __str__(self):
        return "Book ID: {} | Title: {} | Author: {}".format(self.book_id, self.title, self.author)

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


book = Book('The Lord of the Rings', 'J.R.R. Tolkien')
print(book)
