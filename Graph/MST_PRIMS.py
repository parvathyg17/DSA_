import heapq
def MST(graph,start):
  visited=set()
  min_heap=[(0,start)]
  total_weight=0
  while min_heap:
    w,v=heapq.heappop(min_heap)
    if v in visited:
      continue
    visited.add(v)
    total_weight+=w
    for n,edge_weight in graph[v]:
      if n not in visited:
        heapq.heappush(min_heap,(edge_weight,n))
  if len(visited)!=len(graph):
    print("graph is disconnected")
    return
  print("MST Total Weight:", total_weight)

graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

MST(graph, "A")