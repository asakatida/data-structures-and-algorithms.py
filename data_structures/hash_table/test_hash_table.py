from pytest import raises


def test_empty_hash_table_length(new_hash_table):
    assert len(new_hash_table) == 0
    assert isinstance(new_hash_table.buckets, list)


def test_empty_hash_table_contains(new_hash_table):
    with raises(TypeError):
        assert 0 not in new_hash_table
    new_hash_table.set('None', 0)
    with raises(TypeError):
        assert 0 in new_hash_table


def test_data_hash_table_contains(filled_hash_table):
    with raises(TypeError):
        assert 9 in filled_hash_table
    with raises(TypeError):
        assert (12 in filled_hash_table) is False
    with raises(TypeError):
        assert 6 in filled_hash_table
    with raises(TypeError):
        assert 1 in filled_hash_table


def test_empty_hash_table_set(new_hash_table):
    new_hash_table.set('None', 1)
    assert len(new_hash_table) > 0
    with raises(TypeError):
        assert 1 in new_hash_table


def test_data_hash_table_has_length(filled_hash_table):
    assert len(filled_hash_table) > 0


def test_data_hash_table_set_changes_length(filled_hash_table):
    start_len = len(filled_hash_table)
    filled_hash_table.set('11', -1)
    filled_hash_table.set('12', -2)
    assert len(filled_hash_table) - start_len == 2
    with raises(TypeError):
        assert -2 in filled_hash_table


def test_data_hash_table_set_negative_left(filled_hash_table):
    filled_hash_table.set('None', -1)
    with raises(TypeError):
        assert -1 not in filled_hash_table


def test_bad_hash_contains(bad_hash_table):
    assert 'abcd' in bad_hash_table
    assert 'edba' in bad_hash_table
