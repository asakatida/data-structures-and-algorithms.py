from .stack import Stack


class Queue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def __len__(self):
        return len(self.left) + len(self.right)

    def __repr__(self):
        return ''

    def __str__(self):
        return ''

    def dequeue(self):
        pass

    def enqueue(self, value):
        pass
