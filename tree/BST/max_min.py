from collections import deque
class Node:
  def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None
def insert(root,val):
  if root is None:
    return Node(val)
  if val<root.data:
    root.left=insert(root.left,val)
  elif val>root.data:
    root.right=insert(root.right,val)
  return root
  
  
def find_min(root):
  if root is None:
    return None
  if root.left is None:
    return root.data
  return find_min(root.left)
def find_max(root):
  if root is None:
    return None
  if root.right is None:
    return root.data
  return find_max(root.right)

  


root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)

print(find_min(root))
print(find_max(root))