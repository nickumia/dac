import os
import pytest

from dac.process.csv import Csv
from dac.core.data import Data

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_csv_process():
    a = Csv()
    a.has_header = True
    a.addInput(filepath+'test.csv')
    a.extract()

    assert len(a.data) == 20


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


def test_csv_process_context():
    a = Csv()
    a.has_header = True
    a.addInput(filepath+'test.csv')
    a.extract()

    d1 = a.data[0]
    c1 = d1.context

    assert len(c1) == 3
    assert c1[0].focus == 1
    assert c1[0].background == 'odd'

    da = Data()
    da.assignType(list)
    da.setValue([1, 2, 1, True])
    assert c1[1].focus == 1
    assert_data_equal(c1[1].background, da)

    assert c1[2].focus == 1
    assert c1[2].background == 0


def assert_data_equal(obj1, obj2):
    obj1_type = obj1.type
    obj1_value = obj1.getValue()
    obj1_context = obj1.getContext()

    obj2_type = obj2.type
    obj2_value = obj2.getValue()
    obj2_context = obj2.getContext()

    assert obj1_type == obj2_type
    assert obj1_value == obj2_value
    try:
        assert obj1_context == obj2_context
    except AssertionError:
        assert_context_equal(obj1_context, obj2_context)
