class Graph:
  def __init__(self):
    self.graph={}
  def add_vertex(self,vertex):
    if vertex not in self.graph:
      self.graph[vertex]=[]
  def add_edge(self,vertex1,vertex2):
    self.add_vertex(vertex1)
    self.add_vertex(vertex2)

    self.graph[vertex1].append(vertex2)
  def display(self):
    for v,n in self.graph.items():
      print(v,"->",n)
  def indegree(self,vertex):
    count=0
    for n in self.graph.values():
      count+=n.count(vertex)
    return count
  def outdegree(self,vertex):
    if vertex not in self.graph:
      return 0
    return len(self.graph[vertex])
  def degree(self,vertex):
    return self.indegree(vertex)+self.outdegree(vertex)

g = Graph()

g.add_edge("A", "B")
g.add_edge("C", "B")
g.add_edge("B", "D")

g.display()

print("Indegree of B:", g.indegree("B"))
print("Outdegree of B:", g.outdegree("B"))
print("Total degree of B:", g.degree("B"))
      