from collections import deque

def rev_queue(queue):
  stack=[]
  while queue:
    stack.append(queue.popleft())
  while stack:
    queue.append(stack.pop())

q=deque([10,20,30,40])
rev_queue(q)
print(q)