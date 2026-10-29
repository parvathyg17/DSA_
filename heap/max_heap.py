class Max_heap:
  def __init__(self):
    self.heap=[]
  def insert(self,val):
    self.heap.append(val)
    self.heapify_up(len(self.heap)-1)
  def heapify_up(self,i):
    while i>0:
      parent=(i-1)//2
      if self.heap[i]<=self.heap[parent]:
        break
      self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
      i=parent
  def delete(self):
    if not self.heap:
      return None
    if len(self.heap)==1:
      return self.heap.pop()
    max_val=self.heap[0]
    self.heap[0]=self.heap.pop()
    self.heapify_down(0)
    return max_val
  def heapify_down(self,i):
    n=len(self.heap)
    while True:
      largest=i
      left=(2*i)+1
      right=(2*i)+2
      if left<n and self.heap[left]>self.heap[largest]:
        largest=left
      if right<n and self.heap[right]>self.heap[largest]:
        largest=right
      if largest==i:
        break
      self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]

      i=largest
  def peek(self):
    if not self.heap:
      return None
    return self.heap[0]

s=Max_heap()
arr=[3, 8, 5, 12, 10, 7]
for i in range(len(arr)):
  s.insert(arr[i])
print(s.heap)
print(s.delete())
print(s.heap)