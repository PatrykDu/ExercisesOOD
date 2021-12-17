import datetime


class Note:

    def __init__(self, content):
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
        self.content = content


note1 = Note('My first note.')
note2 = Note('My second note.')
