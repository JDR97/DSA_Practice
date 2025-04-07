#Topological Sorting using BFS also known as kahn's Algorithm
#by repeatedly finding vertices with no incoming edges, removing them from 
# the graph, and updating the incoming edges of the vertices connected from the removed 
# removed edges. This process continues until all vertices have been ordered.
#Example: Data processing in the pipeline, Circuit design
#How to count In-Degree? -> Iterate through all the edges in the graph and increment the 
# in-degree of the destination node for each edge
from collections import deque

def constructAdj(v, edges):
    adj =[[] for _ in range(v)]

    for it in edges:
        adj[it[0]].append(it[1])

    return adj

def topologicalSort(v, edges):
    adj = constructAdj(v, edges)
    indegrees = [0]*v

    for u in range(v):
        for w in adj[u]:
            indegrees[w] += 1

    q = deque([i for i in range(v) if indegrees[i] == 0])

    res = []
    while q:
        node = q.popleft()
        res.append(node)

        for neighbor in adj[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.append(neighbor)

    ##Checking for cycle
    if len(res) != v:
        print("Graph has a cycle..")
        return []
        
    return res


if __name__ == "__main__":
    V = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    result = topologicalSort(V, edges)
    if result:
        print("Topological Order:", result)
