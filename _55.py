class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    @staticmethod
    def display_protected_attrs():
        for atr in laptop.__dict__.keys():
            if not atr.startswith('_{}'.format(__class__.__name__)) and atr[0] == '_':
                print(atr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_protected_attrs()
