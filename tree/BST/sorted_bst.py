class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def sorted_to_bst(arr):
  def build(left,right):
    if left>right:
      return None
    mid=(left+right)//2
    root=Node(arr[mid])
    root.left=build(left,mid-1)
    root.right=build(mid+1,right)
    return root
  return build(0,len(arr)-1)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


arr = [50, 30, 70, 20, 40, 60, 80]

root = sorted_to_bst(arr)
inorder(root)