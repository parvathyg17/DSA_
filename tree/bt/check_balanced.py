class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def is_balanced(root):
  def check_height(node):
    if node is None:
      return -1
    left=check_height(node.left)
    if left==-2:
      return -2

    right=check_height(node.right)
    if right==-2:
      return -2
    if abs(left-right)>1:
      return -2
    return 1+ max(left,right)
  return check_height(root)!=-2
      

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

print(is_balanced(root))


    