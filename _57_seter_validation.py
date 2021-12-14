class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        if not price > 0:
            raise TypeError('The price attribute must be a positive int or float value')
        else:
            self._price = price


laptop = Laptop(3499)
try:
    laptop.set_price('-3000')
except TypeError as error:
    print(error)
