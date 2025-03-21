from commons import Graph
from collections import defaultdict, deque


def dijsktra_algorithm(graph: Graph, source):
    distances = defaultdict(lambda: float("inf"))
    queue = deque([])

    distances[source] = 0

    queue.append((distances[source], source))

    while queue:
        distance, node = queue.popleft()

        if distance > distances[node]:
            continue

        for adj_node in graph.edges[node]:
            current_distance = distance + adj_node[1]
            if current_distance < distances[adj_node[0]]:
                distances[adj_node[0]] = current_distance
                queue.append((current_distance, adj_node[0]))
    return distances


if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4, 5])
    graph.add_edge(1, 0, weight=3)
    graph.add_edge(2, 0, weight=4)
    graph.add_edge(1, 3, weight=1)
    graph.add_edge(3, 4, weight=2)
    graph.add_edge(4, 5, weight=1)
    graph.add_edge(2, 5, weight=2)
    graph.add_edge(0, 3, weight=1)

    source = 0
    result = dijsktra_algorithm(graph, source)

    print(f"Min Distances from Node {source}")
    for vertex in graph.vertices:
        print(f"Min Distance from {source} to {vertex} => {result[vertex]}")
