from .print_level_order import print_level_order


def test_empty_k_tree_print_level_order(new_k_tree):
    assert print_level_order(new_k_tree) == '''\
'''


def test_data_k_tree_print_level_order(filled_k_tree):
    assert print_level_order(filled_k_tree) == '''\
1
2 3 4
5 6 7
8 9'''


def test_list_k_tree_print_level_order(linked_list_k_tree):
    assert print_level_order(linked_list_k_tree) == '''\
10
4
3
2
5
7
6
9
8'''
