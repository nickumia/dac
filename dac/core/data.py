
class Data(object):

    def __init__(self):
        self.type = None
        self.value = None
        self.connections = None
        self.context = []

    def assignType(self, definition):
        self.type = definition

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def addContext(self, point, details):
        self.context.append(Context(point, details))

    def getContext(self):
        return self.context


class Context(object):

    def __init__(self, f, b):
        self.focus = f
        self.background = b
