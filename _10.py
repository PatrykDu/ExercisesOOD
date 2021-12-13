def stick(*args) -> str:
    output = [arg for arg in args if type(arg) == str]
    return '#'.join(output)


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))
