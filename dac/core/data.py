
class Data(object):

    def __init__(self):
        self.type = None
        self.value = None
        self.connections = None
        self.context = None

    def assignType(self, definition):
        self.type = definition

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
