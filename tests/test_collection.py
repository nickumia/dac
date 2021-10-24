import os
import pytest

from dac.configure.collection import Collection

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_configure_collection_two_csv_load():
    a = Collection()
    a.add(filepath+'example_config.dac')
    a.mutate()
    results = a.read()
    assert len(results) == 2
