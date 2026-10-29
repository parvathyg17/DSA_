class circularqueue:
  def __init__(self,capacity):
    self.capacity=capacity
    self.queue=[None]*capacity
    self.front=0
    self.rear=0
    self.size=0
  def enqueue(self,val):
    if self.capacity==self.size:
      print("capacity reached")
      return False
    self.queue[self.rear]=val
    self.rear=(self.rear+1)%self.capacity
    self.size +=1
    return True
  def dequeue(self):
    if self.size==0:
      return None
    value=self.queue[self.front]
    self.queue[self.front]=None
    self.front=(self.front+1)%self.capacity
    self.size-=1
    return value
    
cq=circularqueue(4)

cq.enqueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
s=cq.dequeue()
print(s)
cq.enqueue(40)
print(cq.queue)