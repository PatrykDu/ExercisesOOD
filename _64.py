class Person:

    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def del_first_name(self):
        del self._first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.set_first_name(value)

    @first_name.deleter
    def first_name(self):
        self.del_first_name()


person = Person('Tom')
del person.first_name
print(person.__dict__)
