
from dac.configure.csv import CSVResource
from dac.configure.parser import Parser
from dac.core.data import Data


class Collection(object):

    def __init__(self):
        self.parser = Parser()
        self.inputs = {}
        self.memory = {}

    def add(self, afile):
        self.parser.addFile(afile)
        self.inputs = self.parser.parse()

    def mutate(self):
        for name, inp in self.inputs.items():
            if inp['resource'] == 'csv_resource':
                self.memory[name] = CSVResource(**inp['data'])

    def read(self):
        return self.memory

    def mergeRows(self, first, second, impartial=False):
        obj_1 = self.memory[first]
        obj_2 = self.memory[second]

        if (obj_1.getAttributes() == obj_2.getAttributes()) | impartial:
            return obj_1.getRows() + obj_2.getRows()
        else:
            new_rows = []
            obj_1_attributes = obj_1.getAttributes()
            obj_2_attributes = obj_2.getAttributes()
            obj_1_rows = obj_1.getRows()
            obj_2_rows = obj_2.getRows()

            for row in obj_1_rows:
                new_row = Data()
                new_row.assignType(row.readType())
                new_row_value = row.getValue()
                for key,attrib in obj_2_attributes.items():
                    if attrib not in obj_1_attributes.values():
                        new_row_value.append(None)
                new_row.setValue(new_row_value)
                new_rows.append(new_row)

            for row in obj_2_rows:
                new_row = Data()
                new_row.assignType(row.readType())
                new_row_value = row.getValue()
                for key,attrib in obj_1_attributes.items():
                    if attrib not in obj_2_attributes:
                        new_row_value.insert(0, None)
                new_row.setValue(new_row_value)
                new_rows.append(new_row)

            return new_rows
