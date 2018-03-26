from .node import Node


class LLError(Exception):
    """Exception detailing errors from LinkedList methods."""


class LinkedList:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None
        self._size = 0

        for value in reversed(it):
            self.insert(value)

    def __add__(self, value):
        return NotImplemented

    def __contains__(self, value):
        """
        Return a boolean indicating if the value is found in the list.
        """
        return self.find(value)

    def __delitem__(self, value):
        raise NotImplementedError

    def __eq__(self, value):
        return NotImplemented

    def __ge__(self, value):
        return NotImplemented

    def __getitem__(self):
        raise NotImplementedError

    def __gt__(self, value):
        return NotImplemented

    def __iadd__(self, value):
        return NotImplemented

    def __imul__(self, value):
        return NotImplemented

    def __iter__(self):
        """
        """
        node = self.head
        while node is not None:
            yield node.value
            node = node._next

    def __le__(self, value):
        return NotImplemented

    def __len__(self):
        """
        Return the number of values currently in the list.
        """
        return self._size

    def __lt__(self, value):
        return NotImplemented

    def __mul__(self, value):
        return NotImplemented

    def __ne__(self, value):
        return NotImplemented

    def __repr__(self):
        """
        Return a formatted string representing list.
        """
        return f'LinkedList(({ ", ".join(map(repr, self)) }))'

    def __reversed__(self):
        raise NotImplementedError

    def __rmul__(self, value):
        return NotImplemented

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __str__(self):
        """
        Return a string representing list contents.
        """
        return f'[{ ", ".join(map(str, self)) }]'

    def append(self, value):
        """
        Insert a value at the end of the list.
        """
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node._next is not None:
            node = node._next
        node._next = Node(value)

    def clear(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def count(self, value):
        raise NotImplementedError

    def extend(self, it):
        raise NotImplementedError

    def find(self, value):
        """
        Return a boolean indicating if the value is found in the list.
        """
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node._next
        return False

    def index(self, value, start=0, stop=-1):
        raise NotImplementedError

    def insert(self, value):
        """
        Insert a value into the head of the list.
        """
        self.head = Node(value, self.head)
        self._size += 1

    def insert_after(self, key, value):
        """
        Insert a value after the node containing key.
        """
        node = self.head
        while node is not None:
            if node.value == key:
                node._next = Node(value, node._next)
                return
            node = node._next
        raise LLError('insert_after key not in LinkedList')

    def pop(self, index=0):
        raise NotImplementedError

    def remove(self, value):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def sort(self):
        raise NotImplementedError

    __hash__ = None
