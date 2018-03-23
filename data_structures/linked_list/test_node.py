def test_empty_node(new_node):
    assert new_node.value is None
    assert new_node._next is None


def test_chained_node(chained_node):
    assert chained_node.value is 1
    assert chained_node._next is not None


def test_node_repr(new_node):
    assert repr(new_node) == 'None'


def test_node_repr_chain(chained_node):
    assert repr(chained_node) == '1'
    assert repr(chained_node._next) == '2'
