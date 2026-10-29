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
def is_valid(root):
  def validate(node,minimum,maximum):
    if node is None:
      return True
    if node.data<=minimum or node.data>=maximum:
      return False
    left=validate(node.left,minimum,node.data)
    right=validate(node.right,node.data,maximum)
    return left and right
  return validate(root,float("-inf"),float("inf"))

root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)
print(is_valid(root))
  
    
    