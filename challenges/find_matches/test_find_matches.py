from .find_matches import find_matches


def extract_values(_in):
    return [node.value for node in _in]


def test_empty_k_tree_find_matches(new_k_tree):
    assert find_matches(new_k_tree, 1) == []
    assert find_matches(new_k_tree, "1") == []
    assert find_matches(new_k_tree, None) == []


def test_data_k_tree_find_matches(filled_k_tree):
    assert extract_values(find_matches(filled_k_tree, 1)) == [1]
    assert extract_values(find_matches(filled_k_tree, 2)) == [2]


def test_list_k_tree_find_matches(linked_list_k_tree):
    assert extract_values(find_matches(linked_list_k_tree, 3)) == [3]
    assert extract_values(find_matches(linked_list_k_tree, 10)) == [10]


def test_single_k_tree_find_matches(non_unique_k_tree):
    assert extract_values(find_matches(non_unique_k_tree, 2)) == [
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
    ]
    assert extract_values(find_matches(non_unique_k_tree, 3)) == []
