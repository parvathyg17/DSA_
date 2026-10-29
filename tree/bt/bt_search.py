from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None


def search(root,target):
  
  if root is None:
    return False
  if root.data==target:
    return True
  return search(root.left,target) or search(root.right,target)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

print(search(root,10))
