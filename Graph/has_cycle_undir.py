class Graph:
  def __init__(self):
    self.graph={}
  def cycle_exist(self):
    visited=set()
    def dfs(node,parent):
      visited.add(node)
      for n in self.graph[node]:
        if n not in visited:
          if dfs(n,node):
            return True
        elif n !=parent:
          return True
      return False
    for node in self.graph:
      if node not in visited:
        if dfs(node,None):
          return True
    return False
          

g = Graph()


g.graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": []
}

print("Cycle exists:", g.cycle_exist())