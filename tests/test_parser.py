import os

from dac.configure.parser import Parser

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_configure_parser():
    a = None
    with open(filepath+'example_config.dac', 'r') as config:
        a = Parser(config.read())
    results = a.parse()
    name_id = 'csv_resource.test'
    name_id2 = 'csv_resource.test_no_header'
    assert len(results) == 4
    assert len(results[name_id]) == 2
    assert results[name_id]['data']['has_header'] == True
    assert len(results[name_id2]) == 2
    assert results[name_id2]['data']['has_header'] == False
