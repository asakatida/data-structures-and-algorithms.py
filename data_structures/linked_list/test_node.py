def test_empty_node(new_node):
    assert new_node.value is None
    assert new_node._next is None


def test_node_repr(new_node):
    assert repr(new_node) == 'None'
