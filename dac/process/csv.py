import csv

from dac.process.general import Resource
from dac.core.data import Data
from dac.core.types import assume_type, convert_type


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
                    data_type = assume_type(row)
                    row_typed = []
                    for k in row:
                        assumed = assume_type(k)
                        row_typed.append(convert_type(assumed, k))
                    e.assignType(data_type)
                    e.setValue(convert_type(data_type, row_typed))
                    self.records.append(e)

                    for j, column in enumerate(row):
                        d = Data()
                        data_type = assume_type(column)
                        d.assignType(data_type)
                        d.setValue(convert_type(data_type, column))
                        d.addContext(convert_type(data_type, column), self.attributes[j])
                        if self.has_header:
                            d.addContext(convert_type(data_type, column), self.records[i-1])
                        else:
                            d.addContext(convert_type(data_type, column), self.records[i])
                        if len(self.data) == 0:
                            d.addContext(convert_type(data_type, column), 0)
                        else:
                            if self.has_header:
                                d.addContext(convert_type(data_type,column),self.data[((i-1)*len(self.attributes))+j-1]) # NOQA
                            else:
                                d.addContext(convert_type(data_type, column),self.data[(i*len(self.attributes))+j-1]) # NOQA
                        self.data.append(d)
        except BaseException:
            raise Exception('Please use `addInput` to define the input csv '
                            'file first.')

    def inspect_header(self, suspected_header):
        header = {}
        for i, element in enumerate(suspected_header):
            header[i] = element
        return header
