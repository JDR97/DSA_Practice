##BFS for Disconnected Undirected graph
from collections import deque

def bfs_process(adj, s, visited, res):
    q = deque()

    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return res

def bfs(adj):
    v = len(adj)
    res = []
    visited = [False] * v

    for i in range(v):
        if not visited[i]:
            bfs_process(adj, i, visited, res)

    return res

if __name__ == "__main__":
    adj = [[1, 2], [0], [0],
        [4], [3, 5], [4]]
    ans = bfs(adj)
    for i in ans:
        print(i, end=" ")