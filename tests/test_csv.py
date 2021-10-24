import os
import pytest

from dac.process.csv import Csv

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_csv_process():
    a = Csv()
    a.has_header = True
    a.addInput(filepath+'test.csv')
    a.extract()

    assert len(a.data) == 15


def test_csv_process_no_header():
    a = Csv()
    a.addInput(filepath+'test_no_header.csv')
    a.extract()

    assert len(a.data) == 9


def test_csv_process_no_file():
    a = Csv()
    with pytest.raises(Exception):
        a.extract()


def test_csv_process_no_header_record_count():
    a = Csv()
    a.addInput(filepath+'test_no_header.csv')
    a.extract()

    assert len(a.records) == 3
