class OnlineShop:

    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


OnlineShop.country = 'Poland'

print([key for key in OnlineShop.__dict__.keys() if not key.startswith('_')])