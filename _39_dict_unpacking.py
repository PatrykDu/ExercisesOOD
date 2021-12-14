class Book:
    language = 'ENG'
    is_ebook = True


books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
]

book1 = Book()
book2 = Book()

books = [book1, book2]

for book, data in zip(books, books_data):
    for k, v in data.items():
        book.__setattr__(str(k), v)

print(book1.__dict__)
print(book2.__dict__)
