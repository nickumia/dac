
from dac.configure.csv import CSVResource
from dac.configure.parser import Parser

class Collection(object):

    def __init__(self):
        self.parser = Parser()
        self.inputs = {}
        self.memory = {}

    def add(self, afile):
        self.parser.addFile(afile)
        self.inputs = self.parser.parse()

    def mutate(self):
        for name,inp in self.inputs.items():
            if inp['resource'] == 'csv_resource':
                self.memory[name] = CSVResource(**inp['data'])

    def read(self):
        return self.memory

    def mergeRows(self, first, second):
        obj_1 = self.inputs[first]
        obj_2 = self.inputs[second]

        return obj_1.get_rows() + obj_2.get_rows()
