from collections import defaultdict


class CycleExistsException(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Cycle exists in graph."):
        self.message = message
        super().__init__(self.message)


class Graph:
    def __init__(self, vertices=None):
        if not vertices:
            vertices = []
        self.vertices = vertices
        self.edges = defaultdict(list)

    def add_vertices(self, node: int):
        self.vertices.append(node)

    def add_edge(self, source, target, weight=None, directed=True):
        if not weight:
            self.edges[source].append(target)
            if not directed:
                self.edges[target].append(source)
            return
        self.edges[source].append((target, weight))
        if not directed:
            self.edges[target].append((source, weight))

