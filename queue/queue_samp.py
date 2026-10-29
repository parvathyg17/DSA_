class queue:
  def __init__(self):
    self.queue=[]
  def enqueue(self,val):
    self.queue.append(val)
  def dequeue(self):
    if not self.queue:
      return None
    return self.queue.pop(0)

  def peek(self):
    if not self.queue:
      return None
    return self.queue[0]
  def is_empty(self):
    return len(self.queue)==0
    
    
q=queue()
q.queue=[1,2,3,4,5]
q.enqueue(6)
print(q.queue)
q.dequeue()
print(q.queue)
