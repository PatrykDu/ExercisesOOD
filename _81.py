class Person:
    _instances = []

    def __init__(self):
        Person._instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(cls._instances)


person1 = Person()
person2 = Person()
person3 = Person()

print(Person.count_instances())