from .linked_list import LinkedList


class Node:
    def __init__(self, key, value):
        """
        Initialize new Node with optional next Node.
        """
        self.key = key
        self.value = value

    def __repr__(self):
        """
        Return a formatted string representing Node.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        return f'Node({ self.key !r}, { self.value !r})'

    def __str__(self):
        """
        Return a string representing Node.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        return f'node key: ({ self.key }) value: ({ self.value })'


class HashTable:
    def __init__(self, max_size=1024):
        """
        Initialize new hash table with optional max size.
        """
        self.max_size = max_size
        self.buckets = [None] * self.max_size
        self._size = 0

    def __contains__(self, key):
        """
        Indicate if the value is found in the hash table.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        bucket = self._bucket(key)
        if isinstance(bucket, Node):
            return bucket.key == key
        return key in bucket

    def __len__(self):
        """
        Return the number of values currently in the hash table.
        """
        return self._size

    def __repr__(self):
        """
        Return a formatted string representing hash table.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        return f'KTree(usage={ self._size / self.max_size })'

    def __str__(self):
        """
        Return a string representing hash table contents.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        return f'k-tree usage: { self._size / self.max_size }'

    def _bucket(self, key):
        """
        """
        return self.buckets[self.hash_key(key)]

    def _create_bucket(self, key, value):
        """
        """
        self.buckets[self.hash_key(key)] = value

    def hash_key(self, key):
        """
        Converts a string into a index that fits the table buckets.
        """
        try:
            return sum(map(ord, key)) % len(self.buckets)
        except TypeError:
            pass
        raise TypeError(
            f'key must be a `str` object not { type(key).__name__ }')

    def set(self, key, value):
        """
        Inserts value into buckets under the hash for key.
        """
        bucket = self._bucket(key)
        node = Node(key, value)
        if bucket is None:
            self._create_bucket(key, node)
        elif isinstance(bucket, Node):
            if bucket.key == key:
                bucket.value = value
                return
            self._create_bucket(key, LinkedList([node, bucket]))
        else:  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
            bucket.insert(node)
        self._size += 1

    def get(self, key):
        """
        Returns the value associated with key if in table.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        bucket = self._bucket(key)
        if bucket is None:
            raise KeyError
        if isinstance(bucket, Node):
            if bucket.key == key:
                return bucket.value
            raise KeyError
        for node in bucket:
            if node.key == key:
                return node.value
        raise KeyError

    def remove(self, key):
        """
        Deletes the entry associated with a key.
        """  # 16, 22, 39-41, 53, 59, 94-96, 103-113, 119-126
        bucket = self._bucket(key)
        if isinstance(bucket, Node):
            for node in bucket:
                if node.key == key:
                    pass
        else:
            self._create_bucket(key, None)
        self._size -= 1
