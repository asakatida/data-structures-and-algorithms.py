def fizzbuzztree(tree):
    """
    Transform the node values of the tree to fizzbuzz results.
    """

    def _walk(node):
        if not node:
            return
        _walk(node.right)
        _walk(node.left)
        if node.value % 3 == 0:
            if node.value % 5 == 0:
                node.value = "fizzbuzz"
            else:
                node.value = "fizz"
        elif node.value % 5 == 0:
            node.value = "buzz"
        else:
            node.value = str(node.value)

    _walk(tree.root)
    return tree
