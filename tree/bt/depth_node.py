class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def depth_node(root,target):
  if root is None:
    return -1
  if root.data==target:
    return 0
  left_depth=depth_node(root.left,target)
  if left_depth != -1:
    return left_depth+1
  right_depth=depth_node(root.right,target)
  if right_depth != -1:
    return right_depth+1
  return -1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.right.left = Node(70)

print(depth_node(root, 70))   # 3
print(depth_node(root, 20))   # 1
print(depth_node(root, 100))  # -1

    