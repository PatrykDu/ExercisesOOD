class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


def describe_attrs():
    for atr, val in zip(OnlineShop.__dict__.keys(), OnlineShop.__dict__.values()):
        if not atr.startswith('_'):
            print('{} -> {}'.format(atr, val))


describe_attrs()
