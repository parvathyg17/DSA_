from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def height(root):
  if root is None:
    return -1
  left_height=height(root.left)
  right_height=height(root.right)
  return 1+max(left_height,right_height)

def count_internal_nodes(root):
  if root is None:
    return 0
  if root.left is None and root.right is None:
    return 0
  left_count=count_internal_nodes(root.left)
  right_count=count_internal_nodes(root.right)
  return  1+ left_count +right_count
  
  
    

def count_leaf_nodes(root):
  if root is None:
    return 0
  if root.left is None and root.right is None:
    return 1
  left_count=count_leaf_nodes(root.left)
  right_count=count_leaf_nodes(root.right)
  return left_count +right_count

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

s=height(root)
print("height is",s)
c=count_leaf_nodes(root)
print("nodes leaf count",c)
internal=count_internal_nodes(root)
print(internal)
    