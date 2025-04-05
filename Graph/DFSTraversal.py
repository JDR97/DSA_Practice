##For Undirected Connected Graph

def dfs_Rec(adj, s, visited, res):
    visited[s] = True
    res.append(s)

    for i in range(len(adj)):
        if adj[s][i] == 1 and visited[i] == False:
            dfs_Rec(adj, i, visited, res)

def DFS(adj):
    visited = [False]*len(adj)
    res = []
    #Pass the starting the vertex, here it is 0
    dfs_Rec(adj, 0, visited, res)
    return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1

vertex =  5
adj = [[0]*vertex for _ in range(vertex)]

edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

for s,t in edges:
    add_edge(adj, s , t)

res = DFS(adj)
print(" ".join(map(str, res)))