class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.top=None
    
  def push(self,val):
    new_node=Node(val)
    new_node.next=self.top
    self.top=new_node
    
  def pop(self):
    if self.top is None:
      return "stack is empty"
    value=self.top.data
    self.top=self.top.next
    return value
  def peek(self):
    return self.top.data
    
  def display(self):
    current=self.top
    while current:
      print(current.data)
      current=current.next
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("............")
s.pop()
print("............")
s.display()
s.push(40)
print("............")
s.display()
s.pop()
print("............")
s.display()
print(s.peek())
