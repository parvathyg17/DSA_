from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def sum_of_bt(root):
  if root is None:
    return 0
  sum_left=sum_of_bt(root.left)
  sum_right=sum_of_bt(root.right)
  return root.data+sum_left + sum_right
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left=Node(60)
root.right.right=Node(70)
root.left.left = Node(40)
root.left.right = Node(50)

s=sum_of_bt(root)

print(s)