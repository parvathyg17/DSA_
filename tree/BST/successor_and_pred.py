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
def predecessor(root,key):
  if root is None:
    return None
  if root.data>=key:
    return predecessor(root.left,key)
  right=predecessor(root.right,key)
  if right is not None:
    return right
  return root.data

def successor(root,key):
  if root is None:
    return None
  if root.data<=key:
    return successor(root.right,key)
  left=successor(root.left,key)
  if left is not None:
    return left
  return root.data
root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)

s=predecessor(root,50)
print(s)

su=successor(root,50)
print(su)
    