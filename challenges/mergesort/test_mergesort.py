from .mergesort import mergesort


def test_empty_mergesort():
    assert mergesort([]) == []
