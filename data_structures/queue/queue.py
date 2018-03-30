from .node import Node


class Queue:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None
        self._size = 0

        for value in it:
            self.push(value)

    def enqueue(self, value):
        self.head = Node(value, self.head)
        self._size += 1

    def dequeue(self):
        if not self.head:
            raise IndexError('')
        self._size -= 1
