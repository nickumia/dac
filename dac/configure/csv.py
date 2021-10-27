
from dac.configure.code import Internal
from dac.process.csv import Csv


class CSVResource(Internal):

    def __init__(self, **kwargs):
        self.resources = {
            'input':      kwargs['input'],
            'has_header': kwargs['has_header'],

        }
        self.data = {
            'records':    None,
            'points':     None,
            'attributes': None
        }
        self.populate_data()

    def populate_data(self):
        a = Csv()
        a.has_header = (lambda x: 1 if x == 'true' else 0)\
                       (self.resources['has_header'])
        a.addInput(self.resources['input'])
        a.extract()

        data, records, attributes = a.read()
        self.data['records'] = records
        self.data['points'] = data
        self.data['attributes'] = attributes

    def getRows(self):
        return self.data['records']

    def getAttributes(self):
        return self.data['attributes']

    def getData(self):
        return self.data['points']
