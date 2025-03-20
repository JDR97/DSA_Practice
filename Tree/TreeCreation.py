from collections import deque

def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

def printParents(node, adj, parent):
    if parent == 0:
        print("{}->Root".format(node))
    else:
        print("{}->{}".format(node, parent))

    #DFS
    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)

def printChild(root, adj):
    #Queue for BFS
    q = deque()
    q.append(root)
    vis = [0] * len(adj)

    while(q):
        node = q.popleft()
        vis[node] = 1
        print("{}->".format(node))
        for cur in adj[node]:
            if(vis[cur] == 0):
                print(cur)
                q.append(cur)
        print()

def printLeafNodes(root, adj):
    for i in range(1, len(adj)):
        if(len(adj[i]) == 1 and i != root):
            print(i)

def printDegrees(root, adj):
    for i in range(1, len(adj)):
        print(i, ":")
        if(i == root):
            print(len(adj[i]))
        else:
            print(len(adj[i]) - 1)

root = 1
N = 7
adj = [[] for _ in range(N+1)]

addEdge(1, 2, adj)
addEdge(1, 3, adj)
addEdge(1, 4, adj)
addEdge(2, 5, adj)
addEdge(2, 6, adj)
addEdge(4, 7, adj)

print("Print Parents:\n")
printParents(root, adj, 0)

print("Print Children:\n")
printChild(root, adj)

print("Print the Leaf Nodes:\n")
printLeafNodes(root, adj)

print("Print Degrees:\n")
printDegrees(root, adj)