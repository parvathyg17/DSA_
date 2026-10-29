class MyDeque:

    def __init__(self):
        self.items = []

    def append(self, value):
        self.items.append(value)

    def appendleft(self, value):
        self.items.insert(0, value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def popleft(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def display(self):
        print(self.items)