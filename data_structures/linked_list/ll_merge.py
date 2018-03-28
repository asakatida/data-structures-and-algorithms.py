def merge_lists(aList, bList):
    """
    Merge two lists into one with alternating nodes from each.
    """
    node = a = aList.head
    if not a:
        return bList.head
    b = bList.head
    while a and b:
        a._next, b = b, a._next
        a = a._next
    return node
