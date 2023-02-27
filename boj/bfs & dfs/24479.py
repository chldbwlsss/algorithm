### DFS ###
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]  #이차배열 반복문!!
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    global count
    count += 1
    visited[v] = count
    graph[v].sort()
    for i in graph[v]:
        if(visited[i] == 0):
            dfs(graph, i, visited)

dfs(graph, r, visited)
for i in range(1, len(visited)):
    print(visited[i])