class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

    @staticmethod
    def get_sector():
        return OnlineShop.sector


print(OnlineShop.get_sector())
