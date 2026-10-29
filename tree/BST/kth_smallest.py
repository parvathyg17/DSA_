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
def kth_smallest(root,k):
  arr=[]
  def inorder(node):
    if node is None:
      return
    inorder(node.left)
    arr.append(node.data)
    inorder(node.right)
  inorder(root)
  return arr[k-1]
    
root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)

res=kth_smallest(root,3)
print(res)
    