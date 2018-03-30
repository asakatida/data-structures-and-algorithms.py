def test_empty_stack_default(new_stack):
    assert new_stack.head is None


def test_empty_stack_push(new_stack):
    new_stack.push(0)
    assert new_stack.head.value == 0
