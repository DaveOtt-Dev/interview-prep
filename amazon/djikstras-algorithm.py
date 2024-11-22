import heapq

class Node:
    def __init__(self, v, distance):
        self.v = v
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

# V == # of vertices
# adj == adjacent vertices
# S == 
def dijkstra(V, adj, S):
    print(V)
    print(adj)
    print(S)

    


def main():
    adj = [[] for _ in range(6)]

    V = 6
    E = 5
    u = [0, 0, 1, 2, 4]
    v = [3, 5, 4, 5, 5]
    w = [9, 4, 4, 10, 3]

    for i in range(E):
        edge = [v[i], w[i]]
        adj[u[i]].append(edge)

        edge2 = [u[i], w[i]]
        adj[v[i]].append(edge2)

    S = 1

    result = dijkstra(V, adj, S)
    print(result)

if __name__ == "__main__":
    main()