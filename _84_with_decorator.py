import time


class Container:

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S')


print(Container.get_current_time())
