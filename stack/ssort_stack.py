def sort_stack(stack):
  temp=[]
  while stack:
    val=stack.pop()
    while temp and temp[-1]>val:
      stack.append(temp.pop())
    temp.append(val)
  while temp:
    stack.append(temp.pop())
stack=[3, 1, 4, 2]
sort_stack(stack)
print(stack)