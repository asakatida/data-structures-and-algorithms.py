from .queue import Queue


class KTree:
    _POISON = object()

    __slots__ = ('value', 'child', 'sibling', '_size')

    def __init__(self, value=_POISON, sibling=None):
        """
        Initialize new k tree with optional iterable.
        """
        self.value = value
        self.child = None
        self.sibling = sibling
        self._size = 0 if value is self._POISON else 1

    def __contains__(self, value):
        """
        Indicate if the value is found in the k tree.
        """
        if self.value is self._POISON:
            return False
        queue = Queue([self])
        while queue:
            current = queue.dequeue()
            while current is not None:
                if current.child is not None:
                    queue.enqueue(current.child)
                if current.value == value:
                    return True
                current = current.sibling
        return False

    def __len__(self):
        """
        Return the number of values currently in the k tree.
        """
        return self._size

    def __repr__(self):
        """
        Return a formatted string representing k tree.
        """
        if self.value is self._POISON:
            return f'KTree()'
        return f'KTree({ self.value !r}, ...)'

    def __str__(self):
        """
        Return a string representing k tree contents.
        """
        if self.value is self._POISON:
            return f'k-tree root: <blank>'
        return f'k-tree root::value: ({ self.value })'

    def _breadth_first(self, visitor):
        """
        Visit each of the nodes in breadth first order.
        """
        if self.value is self._POISON:
            return
        queue = Queue([self])
        while queue:
            current = queue.dequeue()
            while current is not None:
                if current.child is not None:
                    queue.enqueue(current.child)
                visitor(current)
                current = current.sibling

    def breadth_first(self, visitor):
        """
        Visit each of the values in breadth first order.
        """
        self._breadth_first(lambda node: visitor(node.value))

    def insert(self, parent, value):
        """
        Insert a value into the k tree at all matching parents.
        """
        if self.value is self._POISON:
            self.value = value
            self._size = 1
            return 1

        size = 0

        if self.child is not None:
            size += self.child.insert(parent, value)
        if self.sibling is not None:
            size += self.sibling.insert(parent, value)
        if self.value == parent:
            self.child = KTree(value, self.child)
            size += 1
        self._size += size
        return size

    def post_order(self, visitor):
        """
        Visit each of the values in post order.
        """
        if self.child is not None:
            self.child.post_order(visitor)
        if self.sibling is not None:
            self.sibling.post_order(visitor)
        if self.value is not self._POISON:
            visitor(self.value)

    def pre_order(self, visitor):
        """
        Visit each of the values in pre order.
        """
        if self.value is not self._POISON:
            visitor(self.value)
        if self.child is not None:
            self.child.pre_order(visitor)
        if self.sibling is not None:
            self.sibling.pre_order(visitor)
