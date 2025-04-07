#Topological Sorting using DFS
#What is it? -> USed on Directed Acyclic Graphs, if there is an edge u->v then u should be before v.
#Implementation: Dependency cases, course selection, Makefile, find deadloack, shortest path in DAG, 
#package management system,task scheduling
#Not an unique solution

def constructAdj(v, edges):
    adj = [[] for _ in range(v)]
    for it in edges:
        adj[it[0]].append(it[1])

    return adj

def topoUtil(v, adj, stack, visited):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            topoUtil(i, adj, stack, visited)

    stack.append(v)

def topologicalSort(v, edges):
    stack = []
    visited = [False] * v

    adj = constructAdj(v, edges)

    for i in range(v):
        if not visited[i]:
            topoUtil(i, adj, stack, visited)
    #as stack is not really a stack but list, so appending vertex adds it to end of the list, that is why need reversing.
    return stack[::-1]

if __name__ == '__main__':
    # Graph represented as an adjacency list
    v = 6
    edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]

    ans = topologicalSort(v, edges)

    print(" ".join(map(str, ans)))