import heapq
import math

def dijkstra(graph: dict, start: str):
    """
    Dijkstra's algorithm to find the shortest path from a start node to all other nodes in a graph.

    :param graph: A dictionary representing the graph, where keys are nodes and values are dictionaries of neighbors and edge weights.
    :param start: The starting node.
    :return: A dictionary of shortest distances from the start node to all other nodes.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]


# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node, ":")
for node, distance in shortest_distances.items():
    print(node, ":", distance)