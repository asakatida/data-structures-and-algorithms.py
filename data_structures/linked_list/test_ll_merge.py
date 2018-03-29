from .ll_merge import merge_lists
from .linked_list import LinkedList


def test_empty_list_left(new_list, ordered_list):
    head = merge_lists(new_list, ordered_list)
    assert head is not None
    assert head.value == ordered_list.head.value
    assert head._next.value == ordered_list.head._next.value


def test_empty_list_right(ordered_list, new_list):
    head = merge_lists(ordered_list, new_list)
    assert head is not None
    assert head.value == ordered_list.head.value
    assert head._next.value == ordered_list.head._next.value


def test_unequal_list_len(ordered_list, unordered_list):
    head = merge_lists(ordered_list, unordered_list)
    assert head is not None
    assert head.value == ordered_list.head.value
    assert head._next.value == unordered_list.head.value


def test_unequal_list_len_values_1(ordered_list, unordered_list):
    orig_ordered = LinkedList(tuple(ordered_list))
    orig_unordered = LinkedList(tuple(unordered_list))
    head = merge_lists(ordered_list, unordered_list)
    assert head is not None
    left = orig_ordered.head
    right = orig_unordered.head
    while head:
        if left:
            assert head.value == left.value
            head = head._next
            left = left._next
        if right:
            assert head.value == right.value
            head = head._next
            right = right._next


def test_unequal_list_len_values_2(unordered_list, ordered_list):
    orig_unordered = LinkedList(tuple(unordered_list))
    orig_ordered = LinkedList(tuple(ordered_list))
    head = merge_lists(unordered_list, ordered_list)
    assert head is not None
    left = orig_unordered.head
    right = orig_ordered.head
    while head:
        if left:
            assert head.value == left.value
            head = head._next
            left = left._next
        if right:
            assert head.value == right.value
            head = head._next
            right = right._next
