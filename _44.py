class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_instance_attr(self):
        for atr in self.__dict__.keys():
            print(atr)


laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_instance_attr()
