from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
    
def left_view(root):
  if root is None:
    return []
  queue=deque([root])
  result=[]
  while queue:
    size=len(queue)
    for i in range(size):
      current=queue.popleft()
      if i==0:
        result.append(current.data)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return result

def right_view(root):
  if root is None:
    return []
  queue=deque([root])
  result=[]
  while queue:
    size=len(queue)
    for i in range(size):
      current=queue.popleft()
      if i==size-1:
        result.append(current.data)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return result

  

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
print(left_view(root))
print(right_view(root))


    