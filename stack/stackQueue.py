from collections import deque
class stackQueue:
  def __init__(self):
    self.q1=deque()
    self.q2=deque()

  def push(self,val):
    self.q2.append(val)
    while self.q1:
      self.q2.append(self.q1.popleft())
    self.q1,self.q2=self.q2,self.q1

  def pop(self):
    if not self.q1:
      return None
    return self.q1.popleft()
sq=stackQueue()
sq.push(10)
print(sq.q1)
sq.push(20)
print(sq.q1)
sq.push(30)
print(sq.q1)
sq.pop()
print(sq.q1)