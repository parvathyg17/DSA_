def remove_dup(stack):
  seen=set()
  temp=[]
  while stack:
    val=stack.pop()
    if val not in seen:
      seen.add(val)
      temp.append(val)
  while temp:
    stack.append(temp.pop())
s=[1,3,2,5,8,3,2]
remove_dup(s)
print(s)
  
    