class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Queue:
  def __init__(self):
    self.front=None
    self.rear=None

  def enqueue(self,val):
    new_node=Node(val)
    if self.rear is None:
      self.front=new_node
      self.rear=new_node
      return
    self.rear.next=new_node
    self.rear=new_node
  def dequeue(self):
    if self.front is None:
      return None
    value=self.front.data
    self.front=self.front.next
    if self.front is None:
      self.rear = None
    return value
  def display(self):
    current=self.front
    while current:
      print(current.data)
      current=current.next

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

print("Dequeue:", q.dequeue())

q.display()




