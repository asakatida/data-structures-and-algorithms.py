from .left_join import left_join


def test_tables_abcd_abcd_left_join(abcd_table1, abcd_table2):
    join = left_join(abcd_table1, abcd_table2)
    assert len(join) == len(abcd_table1)
    for key in join:
        assert join.get(key)[1] is not None


def test_tables_efgh_abcd_left_join(efgh_table, abcd_table2):
    join = left_join(efgh_table, abcd_table2)
    assert len(join) == len(efgh_table)


def test_tables_aceg_abcd_left_join(aceg_table, abcd_table2):
    join = left_join(aceg_table, abcd_table2)
    assert len(join) == len(aceg_table)


def test_empty_table_left_left_join(empty_table, abcd_table2):
    join = left_join(empty_table, abcd_table2)
    assert not join


def test_empty_table_right_left_join(empty_table, abcd_table2):
    join = left_join(abcd_table2, empty_table)
    assert len(join) == len(abcd_table2)


def test_empty_tables_left_join(empty_table, abcd_table2):
    join = left_join(empty_table, empty_table)
    assert not join
