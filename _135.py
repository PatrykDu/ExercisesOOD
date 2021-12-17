import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def find(self, text):
        if text.lower() in self.content.lower():
            return True
        else:
            return False


note1 = Note('Object Oriented Programming in Python.')
print(note1.find('python'))
print(note1.find('Python'))
