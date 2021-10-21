import csv

from dac.process.general import Resource
from dac.core.data import Data


class Csv(Resource):

    def __init__(self):
        self.type = 'csv'
        self.extractor = csv.reader
        self.transformer = self.extract
        self.data = []

        self.has_header = False
        self.header = {}
        self.records = []
        self.attributes = {}

    def addInput(self, in_obj):
        self.in_obj = in_obj

    def read(self):
        return self.data, self.records, self.attributes

    def extract(self):
        try:
            with open(self.in_obj, newline='') as csvfile:
                csv_resource = self.extractor(csvfile, delimiter=',')
                for i, row in enumerate(csv_resource):
                    if i == 0:
                        if self.has_header:
                            self.attributes = self.inspect_header(row)
                            continue
                        else:
                            self.attributes = {i: i for i in range(len(row))}
                    e = Data()
                    e.assignType(list)
                    e.setValue(row)
                    self.records.append(e)

                    for j, column in enumerate(row):
                        d = Data()
                        d.assignType(int)
                        d.setValue(column)
                        d.addContext(column, self.attributes[j])
                        self.data.append(d)
        except BaseException:
            raise Exception('Please use `addInput` to define the input csv '
                            'file first.')

    def inspect_header(self, suspected_header):
        header = {}
        for i, element in enumerate(suspected_header):
            header[i] = element
        return header
