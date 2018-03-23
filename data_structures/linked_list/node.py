class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)
