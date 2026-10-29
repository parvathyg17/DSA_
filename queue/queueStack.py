class queueStack:
  def __init__(self):
    self.s1=[]
    self.s2=[]
  def enqueue(self,val):
    self.s1.append(val)
  def dequeue(self):
    if not self.s1 and not self.s2:
      return None
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2.pop()
q = queueStack()


q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.s1)

print("Dequeue:", q.dequeue())
print(q.s2)
