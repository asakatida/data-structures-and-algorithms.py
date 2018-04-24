from .queue import Queue


class Node:
    def __init__(self, val, sibling=None):
        """
        Initialize new Node with optional next Node.
        """
        self.val = val
        self.sibling = sibling
        self.child = None

    def __repr__(self):
        """
        Return a formatted string representing Node.
        """
        return f'Node({ self.val !r})'

    def __str__(self):
        """
        Return a string representing Node.
        """
        return f'node val: ({ self.val })'

    def breadth_first(self, visitor):
        """
        Visit each of the values in breadth first order.
        """
        if self.left:
            self.left.post_order(visitor)
        if self.right:
            self.right.post_order(visitor)
        visitor(self.val)

    def post_order(self, visitor):
        """
        Visit each of the values in post order.
        """
        if self.left:
            self.left.post_order(visitor)
        if self.right:
            self.right.post_order(visitor)
        visitor(self.val)

    def pre_order(self, visitor):
        """
        Visit each of the values in pre order.
        """
        visitor(self.val)
        if self.left:
            self.left.pre_order(visitor)
        if self.right:
            self.right.pre_order(visitor)


class KTree:
    def __init__(self):
        """
        Initialize new k tree with optional iterable.
        """
        self.root = None
        self._size = 0

    def __contains__(self, val):
        """
        Indicate if the val is found in the k tree.
        """
        current = self.root
        while current:
            if current.val == val:
                return True
            if current.val < val:
                current = current.right
            else:
                current = current.left
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
        return f'KTree(root={ self.root !r})'

    def __str__(self):
        """
        Return a string representing k tree contents.
        """
        return f'k-tree root: { self.root }'

    def breadth_first(self, visitor):
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
            visitor(node.val)

    def insert(self, parent, val):
        """
        Insert a val into the k tree.
        """
        if self.root:
            current = self.root
            while True:
                if current.val == val:
                    return
                if current.val > val:
                    if not current.left:
                        current.left = Node(val)
                        self._size += 1
                        return
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(val)
                        self._size += 1
                        return
                    current = current.right
        else:
            self.root = Node(val)
            self._size += 1

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
