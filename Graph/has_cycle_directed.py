class Graph:
  def __init__(self):
    self.graph={}
  def cycle_exist(self):
    visited=set()
    rec_stack=set()
    def dfs(node,parent):
      visited.add(node)
      rec_stack.add(node)
      for n in self.graph[node]:
        if n not in visited:
          if dfs(n,node):
            return True
        elif n in rec_stack:
          return True
      rec_stack.remove(node)
      return False
    for node in self.graph:
      if node not in visited:
        if dfs(node,None):
          return True
    return False
          

g = Graph()

g.graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
    "D": []
}

print("Cycle exists:", g.cycle_exist())