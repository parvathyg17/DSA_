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
def kth_largest(root,k):
  arr=[]
  def rev_inorder(node):
    if node is None:
      return
    rev_inorder(node.right)
    arr.append(node.data)
    rev_inorder(node.left)
  rev_inorder(root)
  if 1<=k <=len(arr):
    return arr[k-1]
  return None
  
root = None

for value in [50, 30, 70, 20, 40, 60, 80,2]:
    root = insert(root, value)

res=kth_largest(root,1)
print(res)
    