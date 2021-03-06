class Laptop:

    def __init__(self, brand, model, price):
        if not isinstance(price, (int, float)) and price > 0:
            raise TypeError('The price attribute must be a positive int or float')

        self.brand = brand
        self.model = model
        self.price = price


laptop = Laptop('Acer', 'Predator', 5490)
print(laptop.__dict__)
