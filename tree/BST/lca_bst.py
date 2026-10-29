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
def lca(root,p,q):
  if root is None:
    return None
  if p<root.data and q<root.data:
    return lca(root.left,p,q)
  elif p>root.data and q>root.data:
    return lca(root.right,p,q)
  else:
    return root
    
root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)

res=lca(root,70,40)
if res:
  print(res.data)
  
    
    