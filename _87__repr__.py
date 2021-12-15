class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return "{}(fname='{}', lname='{}')".format(self.__class__.__name__, self.fname, self.lname)


person = Person('Mike', 'Smith')
print(person)
