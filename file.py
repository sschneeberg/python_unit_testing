class File:
    ''' A file class containing file type, size, and location '''
    def __init__(self, name, ext):
        self.name = name
        self.type = ext
        self.location = 'unsaved'
        self.size = 'unsaved'

    def __str__(self):
        print("{}.{}: {} GB at {}".format(self.name, self.location, self.size, self.location))

    def save_file(self, location):
        if not location: 
            raise ValueError('cannot save to no where')
        else:
            self.size = 1
            self.location = location
            

    def add_to_file(self):
        if type(self.size) == str: 
            self.size = 1
        self.size = self.size + 1




