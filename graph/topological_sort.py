from collections import deque, defaultdict
from commons import Graph, CycleExistsException


def topological_sort_kahn(graph: Graph):
    indegrees = {}

    for vertex in graph.vertices:
        indegrees[vertex] = 0

    for edge_list in graph.edges.values():
        for node in edge_list:
            indegrees[node] += 1

    queue = deque([])
    for node, indegree in indegrees.items():
        if indegree == 0:
            queue.append(node)

    result = []
    while queue:
        node = queue.popleft()

        for adj_node in graph.edges[node]:
            indegrees[adj_node] -= 1

            if indegrees[adj_node] == 0:
                queue.append(adj_node)

        result.append(node)

    if len(result) != len(graph.vertices):
        raise CycleExistsException
    return result


def topological_sort_dfs_util(graph, current_node, visited, result):
    visited[current_node] = True

    for adj_node in graph.edges[current_node]:
        if not visited[adj_node]:
            topological_sort_dfs_util(graph, adj_node, visited, result)

    result.append(current_node)


def topological_dfs(graph: Graph):
    result = []

    visited = defaultdict(lambda: False)

    for vertex in graph.vertices:
        if not visited[vertex]:
            topological_sort_dfs_util(graph, vertex, visited, result)

    return result

if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4, 5])
    graph.add_edge(1, 0)
    graph.add_edge(2, 0)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(2,5)
    # graph.add_edge(4, 1)

    result = topological_sort_kahn(graph)
    result_dfs = topological_dfs(graph)

    print(f"Iterative BFS Approach: {result}")
    print(f"Recursive DFS Approach: {result_dfs[::-1]}")