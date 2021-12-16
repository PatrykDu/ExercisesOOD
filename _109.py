class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def __repr__(self):
        return "{}(category='{}')".format(self.__class__.__name__, self.category)


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    print(instance)
