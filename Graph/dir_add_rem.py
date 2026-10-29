
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbours in self.graph.values():
                if vertex in neighbours:
                    neighbours.remove(vertex)

            del self.graph[vertex]

    def display(self):
        for k, v in self.graph.items():
            print(k, "->", v)


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

print("Original graph:")
g.display()

g.add_vertex("E")
print("\nAfter adding vertex E:")
g.display()

g.add_edge("C", "D")
print("\nAfter adding edge C-D:")
g.display()

g.remove_edge("A", "B")
print("\nAfter removing edge A-B:")
g.display()

g.remove_vertex("C")
print("\nAfter removing vertex C:")
g.display()
