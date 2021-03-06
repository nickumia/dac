
from dac.configure.csv import CSVResource, merge_records, merge_attributes
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
        for name, inp in self.inputs.items():
            if inp['resource'] == 'csv_resource':
                self.memory[name] = CSVResource(**inp['data'])
            if inp['resource'] == 'merge_rows':
                first = inp['data']['first']
                second = inp['data']['second']
                impartial = inp['data']['impartial']
                self.memory[name] = self.mergeRows(first, second, impartial=impartial)  # NOQA E501
            if inp['resource'] == 'merge_columns':
                first = inp['data']['first']
                second = inp['data']['second']
                attribs = inp['data']['attributes'].split(',')
                data = inp['data']['data_only']
                self.memory[name] = self.mergeColumns(first, second, attribs, data=data)  # NOQA E501

    def read(self):
        return self.memory

    def mergeRows(self, first, second, impartial=False):
        obj_1 = self.memory[first]
        obj_2 = self.memory[second]

        if isinstance(obj_1, CSVResource) and isinstance(obj_2, CSVResource):
            return merge_records(obj_1, obj_2, impartial=impartial)

    def mergeColumns(self, first, second, attribs, data=False):
        obj_1 = self.memory[first]
        obj_2 = self.memory[second]

        if isinstance(obj_1, CSVResource) and isinstance(obj_2, CSVResource):
            return merge_attributes(obj_1, obj_2, attribs, data=data)
