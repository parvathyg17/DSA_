class heap:
  def __init__(self):
    self.heap=[]
  def heapify_down(self,i,size=None):
    if size is None:
      size=len(self.heap)
    
    while True:
      smallest=i
    
      left=(2*i)+1
      right=(2*i)+2
      if left<size and self.heap[left]<self.heap[smallest]:
        smallest=left
      if right<size and self.heap[right]<self.heap[smallest]:
        smallest=right
      if smallest==i:
        break
      self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
      i=smallest
  def build_heap(self,arr):
    self.heap=arr.copy()
    n=len(self.heap)
    for i in range(n//2-1,-1,-1):
      self.heapify_down(i)
    return self.heap
  def heap_sort(self, arr):
        self.build_heap(arr)
        n = len(self.heap)

        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]

            self.heapify_down(0, i)

        return self.heap

h = heap()
arr = [10, 5, 20, 2, 8]

print(h.build_heap(arr))
print(h.heap_sort(arr))