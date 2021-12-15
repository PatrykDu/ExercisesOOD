class Pet:

    def __init__(self, name, age):
        if not isinstance(age, int):
            raise TypeError('The value of age must be of type int.')
        if not age > 0:
            raise ValueError('The value of age must be a positive integer.')
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(age, int):
            raise TypeError('The value of age must be of type int.')
        if not age > 0:
            raise ValueError('The value of age must be a positive integer.')
        self._age = value


try:
    pet = Pet('Max', 'seven')
except Exception as error:
    print(error)
