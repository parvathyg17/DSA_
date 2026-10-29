from collections import deque
class StackQueue:
  def __init__(self):
    self.q1=deque()
  def push(self,val):
    self.q1.append(val)
    for i in range(len(self.q1)-1):
      self.q1.append(self.q1.popleft())
  def pop(self):
    if not self.q1:
      return "stack is empty"
    return self.q1.popleft()
sq=StackQueue()
sq.push(10)
sq.push(20)
print(sq.q1)
sq.push(30)
print(sq.q1)
print("popped element",sq.pop())
print(sq.q1)