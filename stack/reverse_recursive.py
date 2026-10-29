def reverse_stack(stack):
  if not stack:
    return
  top=stack.pop()
  reverse_stack(stack)
  insert_bottom(stack,top)

def insert_bottom(stack,val):
  if not stack:
    stack.append(val)
    return
  top=stack.pop()
  insert_bottom(stack,val)
  stack.append(top)
stack=[10,20,30,40]
reverse_stack(stack)
print(stack)