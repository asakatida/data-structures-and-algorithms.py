import shift_array


def test_getLength_of_empty_array():
    assert shift_array.getLength([]) == 0


def test_getLength_of_empty_array_length_one():
    assert shift_array.getLength(['hello world']) == 1


def test_getLength_of_empty_array_length_odd():
    assert shift_array.getLength([None] * 3) == 3


def test_getMiddleOfLength_zero():
    assert shift_array.getMiddleOfLength(0) == 0


def test_getMiddleOfLength_one():
    assert shift_array.getMiddleOfLength(1) == 1


def test_getMiddleOfLength_odd():
    assert shift_array.getMiddleOfLength(3) == 2


def test_yieldItemsWithItem_empty_array():
    assert list(shift_array.yieldItemsWithItem([], list, 1, 0)) == [list]


def test_yieldItemsWithItem_position_at_end():
    assert list(shift_array.yieldItemsWithItem([''], list, 2, 1)) == ['', list]


def test_yieldItemsWithItem_odd_length():
    assert list(shift_array.yieldItemsWithItem(['', ''], list, 3, 1)) == ['', list, '']


def test_yieldItemsWithoutPos_empty_array():
    assert list(shift_array.yieldItemsWithoutPos([], 0, 0)) == []


def test_yieldItemsWithoutPos_position_at_end():
    assert list(shift_array.yieldItemsWithoutPos([''], 1, 0)) == []


def test_yieldItemsWithoutPos_odd_length():
    assert list(shift_array.yieldItemsWithoutPos(['', ''], 2, 1)) == ['']


def test_insertShiftArray_inserts_in_empty_array():
    assert shift_array.insertShiftArray([], None) == [None]


def test_insertShiftArray_inserts_in_odd_array_length():
    assert shift_array.insertShiftArray([None] * 3, 8) == [None, None, 8, None]


def test_insertShiftArray_inserts_in_even_array_length():
    assert shift_array.insertShiftArray([None] * 4, 7) == [None, None, 7, None, None]


def test_insertShiftArray_inserts_in_array_length_one():
    assert shift_array.insertShiftArray([None], 6) == [None, 6]


def test_insertShiftArray_inserts_in_mixed_type_array():
    assert shift_array.insertShiftArray([1, 2, '3', 'FOUR'], 7.5) == [1, 2, 7.5, '3', 'FOUR']
