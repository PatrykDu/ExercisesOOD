class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError('The value of the title attribute must be of str type')
        self.title = title


book = Book()
book.set_title('Inferno')
print(book.title)
