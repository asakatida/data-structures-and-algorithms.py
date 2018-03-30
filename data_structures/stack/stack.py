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

    def peek(self):
        pass

    def pop(self):
        pass

    def push(self, value):
        self.head = Node(value, self.head)
        self._size += 1
