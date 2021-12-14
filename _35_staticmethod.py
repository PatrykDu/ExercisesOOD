class HouseProject:

    number_of_floors = 3
    area = 100

    @staticmethod
    def describe_project():
        print('Floor number: {}'.format(HouseProject.number_of_floors))
        print('Area: {}'.format(HouseProject.area))


HouseProject.describe_project()