import time


class Container:

    def get_current_time():
        return time.strftime('%H:%M:%S')

    get_current_time = staticmethod(get_current_time)


print(Container.get_current_time())
