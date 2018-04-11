from .queue import Queue


class BST:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __iter__(self):
            """
            Iterate through an inorder traversal of the sub tree.
            """
            if self.left:
                yield from self.left
            yield self.value
            if self.right:
                yield from self.right

        def post_order(self, visitor):
            """
            Visit each of the values in post order.
            """
            if self.left:
                self.left.post_order(visitor)
            if self.right:
                self.right.post_order(visitor)
            visitor(self.value)

        def pre_order(self, visitor):
            """
            Visit each of the values in pre order.
            """
            visitor(self.value)
            if self.left:
                self.left.pre_order(visitor)
            if self.right:
                self.right.pre_order(visitor)

        def __repr__(self):
            """
            Return a formatted string representing Node.
            """
            return (
                f'BST._Node({ self.value !r}, '
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
        Initialize new binary search tree with optional iterable.
        """
        self.root = None
        self._size = 0

        for value in it:
            self.insert(value)

    def __contains__(self, value):
        """
        Indicate if the value is found in the binary search tree.
        """
        current = self.root
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
        if self.root:
            yield from self.root

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
        return f'binary search tree root: { self.root }'

    def breadth_first_traversal(self, visitor):
        """
        Visit each of the values in breadth first order.
        """
        if not self.root:
            return
        queue = Queue([self.root])
        while queue:
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            visitor(node.value)

    def insert(self, value):
        """
        Insert a value into the binary search tree.
        """
        if self.root:
            current = self.root
            while True:
                if current.value == value:
                    return
                if current.value > value:
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

    def in_order(self, visitor):
        """
        Visit each of the values in order.
        """
        set(map(visitor, self))

    def post_order(self, visitor):
        """
        Visit each of the values in post order.
        """
        if self.root:
            self.root.post_order(visitor)

    def pre_order(self, visitor):
        """
        Visit each of the values in pre order.
        """
        if self.root:
            self.root.pre_order(visitor)
