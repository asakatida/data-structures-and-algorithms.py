def test_empty_list_length(new_list):
    assert len(new_list) == 0
    assert new_list.head is None


def test_empty_list_insert(new_list):
    new_list.insert(1)
    assert new_list.head is not None


def test_data_list_insert(ordered_list):
    assert ordered_list.head.value == 3
    ordered_list.insert(7)
    assert ordered_list.head.value == 7
    ordered_list.insert(10)
    assert ordered_list.head.value == 10


def test_empty_list_find(new_list):
    assert new_list.find(1) is False
    assert new_list.find('a') is False
    assert new_list.find({}) is False
    assert new_list.find(None) is False


def test_data_list_find(ordered_list):
    assert ordered_list.find(6) is True


def test_data_list_not_find(ordered_list):
    assert ordered_list.find(8) is False
