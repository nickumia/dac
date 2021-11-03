import os

from dac.configure.collection import Collection
from dac.core.data import Data

filepath = '/'.join(os.path.realpath(__file__).split('/')[0:-1]) + '/'


def test_configure_collection_merge_combo2():
    a = Collection()
    a.add(filepath+'merge_columns.dac')
    a.mutate()

    assert 'merge_columns.combo1' in a.memory
    results = a.memory['merge_columns.combo1']
    assert len(results) == 9

#     a1 = Data()
#     a1.assignType(list)
#     a1.setValue([1, 2, 1, True])
#     b1 = Data()
#     b1.assignType(list)
#     b1.setValue([7, 8, 9])
#     assert_data_equal(results[0], a1)
#     assert_data_equal(results[7], b1)

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


def assert_context_equal(con1, con2):
    con1_focus = con1.focus
    con1_background = con1.background

    con2_focus = con2.focus
    con2_background = con2.background

    assert con1_focus == con2_focus
    assert con1_background == con2_background
