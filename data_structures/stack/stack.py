class Stack:
    def __init__(self, it=()):
        """
        Initialize new list with optional iterable.
        """
        self.head = None

        for value in it:
            self.enqueue(value)

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass
