class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def preorder(root):
  if root is None:
      return None
  print(root.data,end=" ")
  preorder(root.left)
  preorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

preorder(root)
    