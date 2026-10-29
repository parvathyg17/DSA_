from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def invert(root):
  if root is None:
    return None
    
  root.left,root.right=root.right,root.left
  invert(root.left)
  invert(root.right)
  return root
def display(root):
  if root is None:
    return -1
  queue=deque([root])
  while queue:
    current=queue.popleft()
    print(current.data,end=" ")
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

root1 = Node(10)
root1.left = Node(20)
root1.right = Node(30)
root1.left.left = Node(40)
root1.left.right = Node(50)
root1.right.left = Node(60)
root1.right.right = Node(70)

invert(root)
display(root)


    