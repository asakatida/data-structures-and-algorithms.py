from .left_join import left_join


def test_empty_tables_left_join():
    assert left_join() is None
