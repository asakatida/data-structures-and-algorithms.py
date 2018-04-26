def find_maximum_value(tree):
    """
    Get the maximum value in the binary tree.
    """
    maximum = None

    def op(val):
        nonlocal maximum
        maximum = val if maximum is None or val > maximum else maximum

    tree.post_order(op)

    return maximum
