from .node import Node


class LinkedList:
    def __init__(self, it=()):
        """
        """
        self.head = None
        self._size = 0

        for value in reversed(it):
            self.insert(value)

    def __add__(self, value):
        pass

    def __contains__(self, value):
        pass

    def __delitem__(self, value):
        pass

    def __eq__(self, value):
        pass

    def __ge__(self, value):
        pass

    def __getitem__(self):
        pass

    def __gt__(self, value):
        pass

    def __iadd__(self, value):
        pass

    def __imul__(self, value):
        pass

    def __iter__(self):
        pass

    def __le__(self, value):
        pass

    def __len__(self):
        """
        """
        return self._size

    def __lt__(self, value):
        pass

    def __mul__(self, value):
        pass

    def __ne__(self, value):
        pass

    def __repr__(self):
        """
        """
        return ''

    def __reversed__(self):
        pass

    def __rmul__(self, value):
        pass

    def __setitem__(self, key, value):
        pass

    def __str__(self):
        """
        """
        return ''

    def append(self, value):
        pass

    def clear(self):
        pass

    def copy(self):
        pass

    def count(self, value):
        pass

    def extend(self, it):
        pass

    def find(self, value):
        """
        """
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node._next
        return False

    def index(self, value, start=0, stop=-1):
        pass

    def insert(self, value):
        """
        """
        self.head = Node(value, self.head)

    def pop(self, index=0):
        pass

    def remove(self, value):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass

    __hash__ = None
