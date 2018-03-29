class Node:
    def __init__(self, value, _next=None):
        """
        Initialize new Node with optional next Node.
        """
        self.value = value
        self._next = _next

    # def __repr__(self):
    #     """
    #     Return a formatted string representing Node.
    #     """
    #     if self._next is None:
    #         return f'Node({ self.value !r})'
    #     return f'Node({ self.value !r}, { self._next !r})'

    def __str__(self):
        """
        Return a string representing Node.
        """
        return f'''({
            self.value
        }, {
            "<END>"if self._next is None else "..."
        })'''
