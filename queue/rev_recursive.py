from collections import deque

def rev_queue(queue):
  if not queue:
    return
  front=queue.popleft()
  rev_queue(queue)
  queue.append(front)

q=deque([40, 30, 20, 10])
rev_queue(q)
print(q)