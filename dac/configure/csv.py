
from dac.configure.code import Internal
from dac.process.csv import Csv

class CSVResource(Internal):

    def __init__(self, **kwargs):
        self.resources = {
            'input'      : kwargs['input'],
            'has_header' : kwargs['has_header'],

        }
        self.populate_data()
        self.data = {
            'records'    : None,
            'points'     : None,
            'attributes' : None
        }

    def populate_data(self):
        a = Csv()
        a.has_header = self.resources['has_header']
        a.addInput(self.resources['input'])
        a.extract()

        data, records, attributes = a.read()
        self.data['records'] = records
        self.data['points'] = points
        self.data['attributes'] = attributes
