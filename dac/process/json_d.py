import json

from dac.process.general import Resource
from dac.core.data import Data
from dac.core.types import assume_type, convert_type


class Json(Resource):

    def __init__(self):
        self.type = 'json'
        self.extractor = json.loads
        self.transformer = self.extract
        self.data = []

        self.records = []
        self.attributes = {}

    def addInput(self, in_obj):
        self.in_obj = in_obj

    def read(self):
        return self.data, self.records, self.attributes

    def extract(self):
        try:
            with open(self.in_obj, newline='') as jsonfile:
                json_resource = self.extractor(jsonfile.read())
                if type(json_resource) == list:
                    for i, element in enumerate(json_resource):
                        # Header element not supported at this time.
                        e = Data()
                        data_type = assume_type(element)
                        element_typed = element
                        e.assignType(data_type)
                        e.setValue(convert_type(data_type, element_typed))
                        self.records.append(e)

                        for key, value in element:
                            e = Data()
                            data_type = assume_type(value)
                            value_typed = value
                            e.assignType(data_type)
                            e.setValue(convert_type(data_type, value_typed))
                            self.data.append(e)

                if type(json_resource) == dict:
                    for key, value in json_resource:
                        e = Data()
                        data_type = assume_type(value)
                        value_typed = value
                        e.assignType(data_type)
                        e.setValue(convert_type(data_type, value_typed))
                        self.data.append(e)
                        
        except BaseException:
            raise Exception('Please use `addInput` to define the input json '
                            'file first.')
