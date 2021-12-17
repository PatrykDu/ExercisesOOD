class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only objects of type str can be added to the list.')
        else:
            super().append(string)


string_list_only = StringListOnly()
string_list_only.append('Data')
string_list_only.append('Science')
print(string_list_only)
