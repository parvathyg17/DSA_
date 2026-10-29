class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def height(root):
  if root is None:
    return -1
  left=height(root.left)
  right=height(root.right)
  return 1+max(left,right)
  
def is_balanced(root):
  if root is None:
    return True
  left=height(root.left)
  right=height(root.right)
  if abs(left-right)>1:
    return False
  return is_balanced(root.left) and is_balanced(root.right)
  
      

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


    