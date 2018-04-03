from .queue import Queue


class AnimalShelter:
    def __init__(self, it=()):
        self.main_queue = Queue(it)
        self.spare_queue = Queue()
        self.spare_type = ''

    def enqueue(self, animal):
        self.main_queue.enqueue(animal)

    def dequeue(self, prefer=None):
        if prefer is None:
            if self.spare_queue:
                return self.spare_queue.dequeue()
            return self.main_queue.dequeue()
        if prefer == self.spare_type:
            return self.spare_queue.dequeue()
        while True:
            top = self.main_queue.dequeue()
            if top == prefer:
                return top
            self.spare_queue.enqueue(top)
            self.spare_type = top
