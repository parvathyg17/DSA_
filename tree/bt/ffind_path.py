from collections import deque
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
 
def find_path(root,target,path):
   if root is None:
     return False
   path.append(root.data)
   if root.data==target:
     return True
    
   if find_path(root.left,target,path) or find_path(root.right,target,path):
     return True
   path.pop()
   return False
   
  
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

path=[]
res=find_path(root,50,path)
if res:
    print(path)
else:
    print("Not found")