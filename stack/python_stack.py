class stack:
  def __init__(self):
    self.stack=[]

  def push(self,val):
    self.stack.append(val)
  def pop(self):
    if not self.stack:
      return None
    return self.stack.pop()
  def peek(self):
    return self.stack[-1]
  def is_empty(self):
    return len(self.stack)==0
  def delete_mid(self):
    temp=[]
    for i in range(len(self.stack)//2):
      temp.append(self.stack.pop())
    x=self.stack.pop()
    while temp:
      self.stack.append(temp.pop())
    return self.stack
  def delete(self,val):
    temp=[]
    while self.stack:
      x=self.stack.pop()
      if x==val:
        break
      temp.append(x)
    while temp:
      self.stack.append(temp.pop())


s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.stack)
print(s.pop())
print(s.stack)
print(s.peek())
print(s.is_empty())