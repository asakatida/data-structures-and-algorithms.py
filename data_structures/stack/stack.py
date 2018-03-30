from .node import Node


class Stack:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None
        self._size = 0

        for value in it:
            self.push(value)

    def __len__(self):
        """
        Return the number of values currently in the stack.
        """
        return self._size

    def peek(self):
        if not self.head:
            raise IndexError('')
        return self.head.value

    def pop(self):
        if not self.head:
            raise IndexError('')
        node = self.head
        self.head = self.head._next
        return node.value

    def push(self, value):
        self.head = Node(value, self.head)
        self._size += 1
