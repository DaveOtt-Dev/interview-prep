def bfs(n, m, edges, s):
    # Write your code here
    print(n,m,edges,s)
    
    edgeDict = {}
    distanceDict = {}
    for i in range(1, n+1):        
        edgeDict[i] = []
        distanceDict[i] = -1
        
    for edge in edges:
        source = edge[0]
        dest = edge[1]
        
        edgeDict[source].append(dest)
        
    currentNodes = edgeDict[s]
    distance = 6
    while len(currentNodes) > 0:
        nextNodes = []
        for currentNode in currentNodes:
            if distanceDict[currentNode] == -1:
                distanceDict[currentNode] = distance
                nextNodes = nextNodes + edgeDict[currentNode]
        currentNodes = nextNodes
        distance += 6
    
    distances = []
    for key in distanceDict:
        if key == s:
            continue
        
        distances.append(distanceDict[key])
        
    return distances



print(bfs(4, 2, [[1, 2], [1, 3]], 1))
print(bfs(3, 1, [[2, 3]], 2))


6,6,-1
-1,6