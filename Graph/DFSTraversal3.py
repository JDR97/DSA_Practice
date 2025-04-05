##DFS traversal for Directed Graph

def add_edge(adj, s, t):
    adj[s].append(t)

def dfs_rec(adj, src, visited):
    visited[src] = True
    print(src, end=" ")
    for i in adj[src]:
        if not visited[i]:
            dfs_rec(adj, i, visited)

def dfs(adj, src):
    visited = [False] * len(adj)
    dfs_rec(adj, src, visited)



if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)