class Car:

    def __init__(self, brand, model, price, type_of_car='sedan'):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car


car = Car('Opel', 'Insignia', 115000)
print(car.__dict__)
