#Adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex, neighbours in self.graph.items():
            print(vertex, "->", neighbours)
    def degree(self,vertex):
        if vertex not in self.graph:
            return 0
        return len(self.graph[vertex])


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

g.display()
s=g.degree("A")
print(s)
