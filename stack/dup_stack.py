class dup_stack:
  def __init__(self):
    self.stack=[]
    self.seen=set()

  def push(self,val):
    if val in self.seen:
      return
    self.stack.append(val)
    self.seen.add(val)
  def pop(self):
    if not self.stack:
      return
    val=self.stack.pop()
    self.seen.remove(val)
    return val
s=dup_stack()
s.push(10)
s.push(20)
s.push(10)
s.push(30)
print(s.stack)