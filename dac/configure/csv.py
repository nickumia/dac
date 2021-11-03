
from dac.configure.code import Internal
from dac.core.data import Data
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
        a.has_header = self.resources['has_header']
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


def merge_records(obj_1, obj_2, impartial=False):
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
            for key, attrib in obj_2_attributes.items():
                if attrib not in obj_1_attributes.values():
                    new_row_value.append(None)
            new_row.setValue(new_row_value)
            new_rows.append(new_row)

        for row in obj_2_rows:
            new_row = Data()
            new_row.assignType(row.readType())
            new_row_value = row.getValue()
            for key, attrib in obj_1_attributes.items():
                if attrib not in obj_2_attributes:
                    new_row_value.insert(0, None)
            new_row.setValue(new_row_value)
            new_rows.append(new_row)

        return new_rows


def merge_attributes(obj_1, obj_2, attribs, data=False):
    obj_1_attributes = obj_1.getAttributes()
    obj_2_attributes = obj_2.getAttributes()
    obj_1_points = obj_1.getData()
    obj_2_points = obj_2.getData()

    objs_with_attribs = []
    for attrib in attribs:
        for point in obj_1_points:
            for context in point.getContext():
                if attrib == context.background:
                    objs_with_attribs.append(point)

        for point in obj_2_points:
            for context in point.getContext():
                if attrib == context.background:
                    objs_with_attribs.append(point)

    if data:
        return objs_with_attribs

    new_rows = []
    for obj in objs_with_attribs:
        for context in obj.getContext():
            if type(context.background) == list:
                new_rows.append(context.background)

    return new_rows
