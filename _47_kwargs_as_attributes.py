class Bucket:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


bucket = Bucket(apple=3.5, milk=2.5, juice=4.9, water=2.5)
print(bucket.__dict__)
