"""
This module detects deadlocks in a resource allocation graph using a simple cycle detection algorithm.
"""

def is_cyclic_util(graph, v, visited, rec_stack):
    visited[v] = True
    rec_stack[v] = True

    for neighbour in graph[v]:
        if not visited[neighbour]:
            if is_cyclic_util(graph, neighbour, visited, rec_stack):
                return True
        elif rec_stack[neighbour]:
            return True

    rec_stack[v] = False
    return False

def detect_deadlock(graph):
    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            if is_cyclic_util(graph, node, visited, rec_stack):
                return True
    return False

if __name__ == "__main__":
    # Dry Run: 0->1, 1->2, 2->0 forms a deadlock (cycle)
    """
      0 ----> 1 ----> 2
      ^             |
      |             |
      | ------------|
    """
    resource_graph = [[1], [2], [0]]
    print("Deadlock detected!" if detect_deadlock(resource_graph) else "No deadlock detected.")
