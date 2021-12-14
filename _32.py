class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


output = [(atr, val) for atr, val in zip(OnlineShop.__dict__.keys(), OnlineShop.__dict__.values()) if not atr.startswith('_')]
for item in output:
    print('{} -> {}'.format(item[0], item[1]))
