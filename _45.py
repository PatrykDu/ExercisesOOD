class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs_with_values(self):
        for k, v in self.__dict__.items():
            print('{} -> {}'.format(k, v))


laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_attrs_with_values()
