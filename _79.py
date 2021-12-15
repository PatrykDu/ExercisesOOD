class Container:

    @classmethod
    def show_details(cls):
        print('Running from {} class.'.format(cls.__name__))


Container.show_details()
