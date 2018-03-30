class Stack:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None

        for value in it:
            self.enqueue(value)

    def peek(self):
        pass

    def pop(self):
        pass

    def push(self, value):
        pass
