from .node import Node


class Queue:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None
        self._size = 0

        for value in it:
            self.enqueue(value)

    def __len__(self):
        """
        Return the number of values currently in the queue.
        """
        return self._size

    def dequeue(self):
        if not self.head:
            raise IndexError('')
        node = self.head
        if not self.head._next:
            self.head = None
            self._size -= 1
            return node.value
        while node._next._next:
            node = node._next
        node._next, node = None, node._next
        self._size -= 1
        return node.value

    def enqueue(self, value):
        self.head = Node(value, self.head)
        self._size += 1
