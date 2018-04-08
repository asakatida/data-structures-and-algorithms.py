class BST:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __iter__(self):
            """
            """
            if self.left:
                yield from self.left
            yield self.value
            if self.right:
                yield from self.right

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
        yield from self.root

    def __len__(self):
        """
        Return the number of values currently in the list.
        """
        return self._size

    def __repr__(self):
        """
        Return a formatted string representing list.
        """
        return f'BST(({ ", ".join(map(repr, self)) }))'

    def __str__(self):
        """
        Return a string representing list contents.
        """
        return f'binary search tree root: { self.root }'

    def insert(self, value):
        """
        Insert a value into the head of the list.
        """
        if self.root:
            current = self.root
            while True:
                if current.value >= value:
                    if not current.left:
                        current.left = BST._Node(value)
                        self._size += 1
                        return
                    current = current.left
                else:
                    if not current.right:
                        current.right = BST._Node(value)
                        self._size += 1
                        return
                    current = current.right
        else:
            self.root = BST._Node(value)
            self._size += 1
