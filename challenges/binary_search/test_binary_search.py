from .binary_search import binary_search


def test_binary_search_empty_array():
    assert binary_search([], 0) == -1


def test_binary_search_not_found_in_short_array():
    assert binary_search([1, 2, 3], 0) == -1


def test_binary_search_found_at_begining():
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0


def test_binary_search_found_at_end():
    assert binary_search([0, 1, 3, 4, 5], 5) == 4


def test_binary_search_found_at_middle_even():
    assert binary_search([0, 1, 3, 5], 3) == 2


def test_binary_search_found_at_middle_odd():
    assert binary_search([1, 3, 5], 3) == 1
