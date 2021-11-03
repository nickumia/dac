import re

from dac.core.types import assume_type, convert_type


class Parser(object):

    def __init__(self, raw=None):
        self.raw = raw
        self.blocks = {}

    def addFile(self, afile):
        with open(afile, 'r') as config:
            self.raw = config.read()

    def isolate(self, multiple):
        return multiple.split('\n----\n\n')

    def parse(self):
        structure = ('(?P<resource>\".*\") (?P<name>\".*\") '
                     '(?P<data>{[\\s\\S]+})')
        pass_0 = self.isolate(self.raw)
        for element in pass_0:
            pass_1 = re.search(structure, element)
            if pass_1 is not None:
                block_data = {}
                block_data_list = pass_1.group('data').split('\n')
                for block in block_data_list:
                    try:
                        key, value = block.split(' = ')
                        key = ''.join(key.split())
                        value = ''.join(value.split()).replace('\"', '')
                        value_type = assume_type(value)
                        block_data[key] = convert_type(value_type, value)
                    except BaseException:
                        # Probably just the start/end {}
                        pass

                name_id = pass_1.group('name').replace('\"', '')
                resource = pass_1.group('resource').replace('\"', '')
                self.blocks['%s.%s' % (resource, name_id)] = {
                    'resource': resource,
                    'data': block_data
                }
        return self.blocks
