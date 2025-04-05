##For Complete traversal of Disconnected Undirected Graph
from collections import defaultdict

##List of list ---> adj
def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)

def dfs_recur(adj, s, visited, res):
    visited[s] = True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfs_recur(adj, i, visited, res)


def dfs(adj):
    visited = [False] * len(adj)
    res = []

    for i in range(len(adj)):
        if not visited[i]:
            dfs_recur(adj, i, visited, res)

    return res

V = 6
# Create an adjacency list for the graph
adj = defaultdict(list)

# Define the edges of the graph
edges = [[1, 2], [2, 0], [0, 3], [4, 5]]

# Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])
res = dfs(adj)

print(' '.join(map(str, res)))