from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def max_bt(root):
  
  if root is None:
    return float("-inf")
  max_left=max_bt(root.left)
  max_right=max_bt(root.right)
  return max(root.data,max_left,max_right)
def min_bt(root):
  
  if root is None:
    return float("inf")
  min_left=min_bt(root.left)
  min_right=min_bt(root.right)
  return min(root.data,min_left,min_right)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

s=max_bt(root)
p=min_bt(root)
print("max node",s)
print("min node",p)