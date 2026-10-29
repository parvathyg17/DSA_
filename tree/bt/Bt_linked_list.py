from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BT:
  def __init__(self):
    self.root=None
  def insert(self,val):
    new_node=Node(val)
    if self.root is None:
      self.root=new_node
      return 
    queue=deque([self.root])
    while queue:
      current=queue.popleft()
      if current.left is None:
        current.left=new_node
        return 
      else:
        queue.append(current.left)
      if current.right is None:
        current.right=new_node
        return
      else:
        queue.append(current.right)

  def display(self):
    if self.root is None:
      print("tree is empty")
      return
    queue=deque([self.root])
    while queue:
      current=queue.popleft()
      print(current.data)
      if current.left is not None:
        queue.append(current.left)
      if current.right is not None:
        queue.append(current.right)
    print()

bt=BT()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)
bt.insert(60)
bt.insert(70)

bt.display()
    
      
      