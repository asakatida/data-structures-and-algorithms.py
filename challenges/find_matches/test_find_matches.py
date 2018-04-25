from .find_matches import find_matches


def test_empty_k_tree_find_matches(new_k_tree):
    assert find_matches(new_k_tree) == []


def test_data_k_tree_find_matches(filled_k_tree):
    assert find_matches(filled_k_tree) == []


def test_list_k_tree_find_matches(linked_list_k_tree):
    assert find_matches(linked_list_k_tree) == []
