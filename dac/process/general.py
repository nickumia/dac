
class Resource():

    def __init__(self):
        self.type = 'general'
        self.extractor = None
        self.transformer = None
        self.data = None

    def add_input(self, in_obj):
        self.in_obj = in_obj

    def read(self):
        pass
