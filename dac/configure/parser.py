import re

from dac.configure.csv import CSVResource


class Parser(object):

    def __init__(self, raw):
        self.raw = raw
        self.blocks = {}

    def isolate(self, multiple):
        return multiple.split('\n----\n\n')

    def parse(self):
        structure = '(?P<resource>\".*\") (?P<name>\".*\") (?P<data>{[\\s\\S]+})'
        pass_0 = self.isolate(self.raw)
        for element in pass_0:
            pass_1 = re.search(structure, element)
            if pass_1 is not None:
                block_data = {}
                block_data_list = pass_1.group('data').split('\n')
                for block in block_data_list:
                    try:
                        key,value = block.split(' = ')
                        key = ''.join(key.split())
                        value = ''.join(value.split())
                        block_data[key] = value
                    except BaseException:
                        # Probably just the start/end {}
                        pass

                self.blocks[pass_1.group('name').replace('\"', '')] = {
                    'resource' : pass_1.group('resource').replace('\"', ''),
                    'data' : block_data
                }
        return self.blocks
