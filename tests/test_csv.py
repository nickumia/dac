import os

from dac.process.csv import Csv

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_csv_num_of_elements():
    a = Csv()
    a.addInput(filepath+'test.csv')
    a.extract()

    assert len(a.data) == 9
