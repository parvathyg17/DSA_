class Graph:
  def __init__(self):
    self.graph={}
  def path_exists(self,start,end):
    if start not in self.graph or end not in self.graph:
      return False
    visited=set()
    path=[]
    def dfs(node):
      visited.add(node)
      path.append(node)
      if node ==end:
        return True
      for n in self.graph[node]:
        if n not in visited:
          if dfs(n):
            return True
      path.pop()
      return False
    f=dfs(start)
    return f,path

g = Graph()

g.graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
    "E": []
}

print(g.path_exists("A", "D"))
print(g.path_exists("A", "E"))
print(g.path_exists("B", "C"))
print(g.path_exists("A", "F"))