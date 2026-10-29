class UniqueStack:

    def __init__(self):
        self.stack = []
        self.seen = set()

    def push(self, value):
        if value in self.seen:
            return False

        self.stack.append(value)
        self.seen.add(value)
        return True

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()
        self.seen.remove(value)
        return value

    def peek(self):
        if not self.stack:
            return None

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

s = UniqueStack()

print(s.push(10))   # True
print(s.push(20))   # True
print(s.push(10))   # False

print(s.stack)