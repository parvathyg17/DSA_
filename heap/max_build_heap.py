class Max_heap:
  def __init__(self):
    self.heap=[]
  def build_heap(self,arr):
    self.heap=arr.copy()
    n=len(self.heap)
    for i in range(n//2-1,-1,-1):
      self.heapify_down(i)
    return self.heap
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
arr = [4, 10, 3, 5, 1]
print(s.build_heap(arr))