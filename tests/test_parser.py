import os

from dac.configure.parser import Parser

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_configure_parser():
    a = None
    with open(filepath+'example_config.dac', 'r') as config:
        a = Parser(config.read())
    results = a.parse()
    assert len(results) == 3
    assert len(results['test']) == 2
    assert results['test']['data']['has_header'] == 'true'
    assert len(results['test_no_header']) == 2
    assert results['test_no_header']['data']['has_header'] == 'false'
