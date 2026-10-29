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

def delete(root,val):
  if root is None:
    return None
  if val<root.data:
    root.left=delete(root.left,val)
  elif val>root.data:
    root.right=delete(root.right,val)
  else:
    if root.left is None and root.right is None:
      return None
    elif root.left is None:
      return root.right
    elif root.right is None:
      return root.left
    successor=root.right
    while successor.left is not None:
      successor=successor.left
    root.data=successor.data
    root.right=delete(root.right,successor.data)
  return root
def inorder(root):
  if root is None:
    return 
  inorder(root.left)
  print(root.data,end=" ")
  inorder(root.right)
  
      

root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)
  

inorder(root)
root=delete(root, 30)

print("\nAfter deletion:")
inorder(root)
