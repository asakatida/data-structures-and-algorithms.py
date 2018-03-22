from .largest_product import largest_product


def test_largest_product_empty_array():
    assert largest_product([]) == 0


def test_largest_product_single_pair():
    assert largest_product([(1, 2)]) == 2


def test_largest_product_early_answer():
    assert largest_product([(1, 2), (2, 2), (2, 1), (1, 1)]) == 4
