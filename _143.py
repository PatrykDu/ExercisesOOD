class CustomDict(dict):

    def is_any_str_value(self):
        for v in self.values():
            if isinstance(v, str):
                return True
        else:
            return False


cd = CustomDict(python='mid')
print(cd.is_any_str_value())
