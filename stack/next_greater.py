def next_greater(arr):
  answer=[-1]*len(arr)
  stack=[]
  for i in range(len(arr)-1,-1,-1):
    while stack and stack[-1]<=arr[i]:
      stack.pop()
    if stack:
      answer[i]=stack[-1]
    stack.append(arr[i])
  return answer

s=next_greater([5,2,10,3])
print(s)
    