class graph:
  def __init__(self):
    self.graph={}
  def add_vertex(self,vertex):
    if vertex not in self.graph:
      self.graph[vertex]=[]
  def add_edge(self,vertex1,vertex2):
    self.add_vertex(vertex1)
    self.add_vertex(vertex2)
    self.graph[vertex1].append(vertex2)
    self.graph[vertex2].append(vertex1)
  def remove_edge(self,vertex1,vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      if vertex2 in self.graph[vertex1]:
        self.graph[vertex1].remove(vertex2)
      if vertex1 in self.graph[vertex2]:
        self.graph[vertex2].remove(vertex1)
  def remove_vertex(self,vertex):
    if vertex in self.graph:
      for n in self.graph[vertex]:
        self.graph[n].remove(vertex)
      del self.graph[vertex]
  def display(self):
    for k,v in self.graph.items():
      print(k,"->",v)
  def dfs(self,start):
    visited=set()
    def visit(vertex):
      if vertex in visited:
        return
      visited.add(vertex)
      print(vertex,end=" ")
      for n in self.graph[vertex]:
        visit(n)
    if start not in self.graph:
      print("not found")
      return
    visit(start)
    
      
g = graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print("Original graph:")
g.display()
g.dfs("A")
    