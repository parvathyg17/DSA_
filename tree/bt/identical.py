class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
# def depth_node(self,target):
#   if root is None:
#     return -1
#   if root.data==target:
#     return 0
#   left_depth=depth_node(root.left,target)
#   if left_depth != -1:
#     return left_depth+1
#   right_depth=depth_node(root.right,target)
#   if right_depth !=1:
#     return right_depth+1
#   return -1

def diameter(root):
  longest=0
  def height(node):
    nonlocal longest
    if  node is None:
      return 0
    left=height(node.left)
    right=height(node.right)
    longest=max(longest,left+right)
    return 1+ max(left,right)
  height(root)
  return longest
def identical(root,root1):
  if root is None and root1 is None:
    return True
  if root is None or root1 is None:
    return False
  return (root.data==root1.data and identical(root.left,root1.left) and identical(root.right,root1.right))
  
      

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

root1 = Node(10)
root1.left = Node(20)
root1.right = Node(30)
root1.left.left = Node(40)
root1.left.right = Node(50)
root1.right.left = Node(60)
root1.right.right = Node(70)


print(identical(root,root1))