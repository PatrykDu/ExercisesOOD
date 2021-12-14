class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    @staticmethod
    def display_private_attrs():
        for atr in laptop.__dict__.keys():
            if atr.startswith('_{}'.format(__class__.__name__)):
                print(atr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
Laptop.display_private_attrs()
