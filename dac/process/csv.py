import csv

from dac.process.general import Resource
from dac.core.data import Data


class Csv(Resource):

    def __init__(self):
        self.type = 'csv'
        self.extractor = csv.reader
        self.transformer = self.extract
        self.data = []

    def addInput(self, in_obj):
        self.in_obj = in_obj

    def read(self):
        return self.data

    def extract(self):
        try:
            with open(self.in_obj, newline='') as csvfile:
                csv_resource = self.extractor(csvfile, delimiter=',')
                for row in csv_resource:
                    for column in row:
                        d = Data()
                        d.assignType(int)
                        d.setValue(column)
                        self.data.append(d)
        except BaseException:
            raise Exception('Please use `addInput` to define the input csv '
                            'file first.')
