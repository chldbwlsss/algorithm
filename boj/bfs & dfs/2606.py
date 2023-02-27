### bfs ###
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start ,visited):
    global count
    visited[start] = True
    queue = deque([start])
    while queue:
        for f in graph[queue.popleft()]:
            if not visited[f]:
                count += 1
                visited[f] = True
                queue.append(f)

bfs(graph, 1, visited)
print(count)
    


