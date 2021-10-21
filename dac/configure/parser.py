import re

from dac.configure.csv import CSVResource


class Parser(object):

    def __init__(self, raw):
        self.raw = raw

    def parse(self):
        structure = '(?P<resource>\".*\") (?P<name>\".*\") (?P<data>{[\s\S]})'
        pass_1 = re.search(structure, self.raw)
        print(self.raw)
        print(pass_1)
        return pass_1.groups()
