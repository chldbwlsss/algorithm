### dfs, bfs ###
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    u, s = map(int, input().split())
    graph[u].append(s)
    graph[s].append(u)

##DFS
def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ') #방문 기록
    for i in sorted(graph[v]):
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

##BFS
def bfs(graph, v, visited_bfs):
    visited_bfs[v] = True
    print(v, end=' ') #방문 기록
    queue = deque([v])
    while queue:
        for i in sorted(graph[queue.popleft()]):
            if not visited_bfs[i]:
                visited_bfs[i] = True
                print(i, end=' ') #방문기록
                queue.append(i)

#실행
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)






