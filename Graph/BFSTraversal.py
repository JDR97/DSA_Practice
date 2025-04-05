#Popular graph algorithms like Dijkstra’s shortest path, Kahn’s Algorithm, and Prim’s algorithm are based on BFS.
#Problems: Detect Cycle, Shortest Path
#Visit nearest/neighbour nodes first, then rest.
from collections import deque
def bfs(adj):
    vertex = len(adj)
    res = []
    s = 0

    q = deque()
    visited = [False] * vertex

    visited[s] = True
    q.append(s)

    while(q):
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return res



if __name__ == "__main__":
    
    # create the adjacency list
    # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    ans = bfs(adj)
    for i in ans:
        print(i, end=" ")


