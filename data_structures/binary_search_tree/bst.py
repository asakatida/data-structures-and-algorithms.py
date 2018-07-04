from .queue import Queue


class BST:
    _POISON = object()

    __slots__ = ('value', 'left', 'right', '_size')

    def __init__(self, it=()):
        """
        Initialize new binary search tree with optional iterable.
        """
        self.value = self._POISON
        self.left = None
        self.right = None
        self._size = 0

        for value in it:
            self.insert(value)

    def __contains__(self, value):
        """
        Indicate if the value is found in the binary search tree.
        """
        if self.value is self._POISON:
            return False
        current = self
        while current:
            if current.value == value:
                return True
            if current.value < value:
                current = current.right
            else:
                current = current.left
        return False

    def __iter__(self):
        """
        Iterate through an inorder traversal of the tree.
        """
        if self.left is not None:
            yield from self.left
        if self.value is not self._POISON:
            yield self.value
        if self.right is not None:
            yield from self.right

    def __len__(self):
        """
        Return the number of values currently in the binary search tree.
        """
        return self._size

    def __repr__(self):
        """
        Return a formatted string representing binary search tree.
        """
        lst = []
        self.pre_order(lst.append)
        return f'BST(({ ", ".join(map(repr, lst)) }))'

    def __str__(self):
        """
        Return a string representing binary search tree contents.
        """
        if self.value is self._POISON:
            return f"binary search tree"
        return f"binary search tree root: { self.value }"

    def breadth_first_traversal(self, visitor):
        """
        Visit each of the values in breadth first order.
        """
        if self.value is self._POISON:
            return
        queue = Queue([self])
        while queue:
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            visitor(node.value)

    def insert(self, value):
        """
        Insert a value into the binary search tree.
        """
        if self.value is self._POISON:
            self.value = value
            self._size = 1
            return 1
        current = self
        while True:
            if current.value == value:
                return 0
            if current.value > value:
                if not current.left:
                    current.left = BST([value])
                    self._size += 1
                    return 1
                current = current.left
            else:
                if not current.right:
                    current.right = BST([value])
                    self._size += 1
                    return 1
                current = current.right

    def in_order(self, visitor):
        """
        Visit each of the values in order.
        """
        set(map(visitor, self))

    def post_order(self, visitor):
        """
        Visit each of the values in post order.
        """
        if self.left is not None:
            self.left.post_order(visitor)
        if self.right is not None:
            self.right.post_order(visitor)
        if self.value is not self._POISON:
            visitor(self.value)

    def pre_order(self, visitor):
        """
        Visit each of the values in pre order.
        """
        if self.value is not self._POISON:
            visitor(self.value)
        if self.left is not None:
            self.left.pre_order(visitor)
        if self.right is not None:
            self.right.pre_order(visitor)
