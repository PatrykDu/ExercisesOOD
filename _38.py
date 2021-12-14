class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]

for book in books:
    for k, v in zip(book.__dict__.keys(), book.__dict__.values()):
        if not k.startswith('_'):
            print('{} -> {}'.format(k, v))
    print('-' * 30)
