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

    def insert(self, val):
        """
        Insert a val as a child of node.
        """
        self.child = Node(val, self.child)

    def post_order(self, visitor):
        """
        Visit each of the values in post order.
        """
        if self.child:
            self.child.post_order(visitor)
        if self.sibling:
            self.sibling.post_order(visitor)
        visitor(self.val)

    def pre_order(self, visitor):
        """
        Visit each of the values in pre order.
        """
        visitor(self.val)
        if self.child:
            self.child.pre_order(visitor)
        if self.sibling:
            self.sibling.pre_order(visitor)


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
        if not self.root:
            return False
        queue = Queue([self.root])
        while queue:
            current = queue.dequeue()
            while current:
                if current.child:
                    queue.enqueue(current.child)
                if current.val == val:
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
        return f'KTree(root={ self.root !r})'

    def __str__(self):
        """
        Return a string representing k tree contents.
        """
        return f'k-tree root: { self.root }'

    def _breadth_first(self, visitor):
        """
        Visit each of the nodes in breadth first order.
        """
        if not self.root:
            return
        queue = Queue([self.root])
        while queue:
            current = queue.dequeue()
            while current:
                if current.child:
                    queue.enqueue(current.child)
                visitor(current)
                current = current.sibling

    def breadth_first(self, visitor):
        """
        Visit each of the values in breadth first order.
        """
        self._breadth_first(lambda node: visitor(node.val))

    def insert(self, parent, val):
        """
        Insert a val into the k tree at all matching parents.
        """
        if not self.root:
            self.root = Node(val)
            self._size += 1
        else:
            def insert(node):
                if node.val == parent:
                    node.insert(val)
                    self._size += 1
            self._breadth_first(insert)

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
