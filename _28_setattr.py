class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'


setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print('brand: {}'.format(Laptop.brand))
print('model: {}'.format(Laptop.model))