from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def level_order(root):
  if root is None:
    return
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
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

level_order(root)
    