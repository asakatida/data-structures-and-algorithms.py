def test_empty_list(new_list):
    assert new_list._size == 0
    assert new_list.__len__() == 0
    assert len(new_list) == 0
    assert new_list.head is None
