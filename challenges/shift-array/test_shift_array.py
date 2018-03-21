import shift_array


def test_insertShiftArray_inserts_in_empty_array():
    assert shift_array.insertShiftArray([], None) == [None]


def test_insertShiftArray_inserts_in_odd_array_length():
    assert shift_array.insertShiftArray([None] * 3, 8) == [None, None, 8, None]


def test_insertShiftArray_inserts_in_even_array_length():
    assert shift_array.insertShiftArray([None] * 4, 7) == [None, None, 7, None, None]


def test_insertShiftArray_inserts_in_array_length_one():
    assert shift_array.insertShiftArray([None], 6) == [None, 6]
