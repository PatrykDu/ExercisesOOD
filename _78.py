class Person:

    @classmethod
    def show_details(cls):
        print('Running from {} class.'.format(cls.__name__))


Person.show_details()
