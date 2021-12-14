class Person:

    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    @property
    def first_name(self):
        return self.get_first_name()

    @first_name.setter
    def first_name(self, value):
        self.set_first_name(value)


person = Person('John')
person.first_name = 'Mike'
print(person.first_name)
