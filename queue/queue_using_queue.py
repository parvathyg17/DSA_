from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.queue)

print(q.dequeue())
print(q.peek())
print(q.is_empty())