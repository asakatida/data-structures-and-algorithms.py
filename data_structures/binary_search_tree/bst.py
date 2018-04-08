class BST:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self):
            """
            Return a formatted string representing Node.
            """
            return (
                f'_Node({ self.value !r}, '
                f'left={ self.left !r}, '
                f'right={ self.right !r})')

        def __str__(self):
            """
            Return a string representing Node.
            """
            return f'''({
                self.value
            }, left={
                "<NONE>"if self.left is None else "..."
            }, right={
                "<NONE>"if self.right is None else "..."
            })'''

    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.root = None
        self._size = 0

        for value in it:
            self.insert(value)

    def __contains__(self, value):
        """
        Return a boolean indicating if the value is found in the list.
        """

    def __iter__(self):
        """
        """

    def __len__(self):
        """
        Return the number of values currently in the list.
        """
        return self._size

    def __repr__(self):
        """
        Return a formatted string representing list.
        """
        return f'LinkedList(({ ", ".join(map(repr, self)) }))'

    def __str__(self):
        """
        Return a string representing list contents.
        """
        return f'[{ ", ".join(map(str, self)) }]'

    def _insert_after(self, node, value):
        node._next = self._Node(value, node._next)
        self._size += 1

    def _insert_head(self, value):
        self.head = self._Node(value, self.head)
        self._size += 1

    def _remove_after(self, node):
        node._next = node._next._next
        self._size -= 1

    def _remove_head(self):
        self.head = self.head._next
        self._size -= 1

    def insert(self, value):
        """
        Insert a value into the head of the list.
        """
        self._insert_head(value)
