def merge_lists(aList, bList):
    """
    Merge two lists into one with alternating nodes from each.
    """
    node = a = aList.head
    if not a:
        return bList.head
    b = bList.head
    a._next = b
    while a and b:
        a = a._next
        b = b._next
    return node
