# tree = [10, 20, 30, 40, 50, 60, 70]
class BT:
  def __init__(self):
    self.tree=[]
  def insert(self,val):
    self.tree.append(val)
  def display(self):
    return self.tree
  def left_sbt(self,i):
    index=(2*i)+1
    if index<len(self.tree):
      return self.tree[index]
  def right_sbt(self,i):
    index=(2*i)+2
    if index<len(self.tree):
      return self.tree[index]
  def parent(self,i):
    if i==0:
      return None
    index=(i-1)//2
    return self.tree[index]
    
    
tree = BT()

for val in [10, 20, 30, 40, 50, 60, 70]:
    tree.insert(val)

print(tree.display())
print(tree.left_sbt(0))
print(tree.right_sbt(0))
print(tree.parent(1))
print(tree.parent(2))
print(tree.left_sbt(2))
print(tree.right_sbt(2))
print(tree.parent(0))