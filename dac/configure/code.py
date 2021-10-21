
class Internal(object):

    def __init__(self):
        self.resources = None
        self.data = None

    def get_resource(self, res):
        if res in self.resources:
            return self.resources[res]
        return None

    def get_data(self, data):
        if data in self.data:
            return self.data[data]
        return None
