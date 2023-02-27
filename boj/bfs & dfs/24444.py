### bfs ###
from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1 #방문 순서를 기록하기 위함

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, now, visited):
    global count
    visited[now] = count #방문처리
    queue = deque([now]) #queue 만들기
    while queue:
        for f in sorted(graph[queue.popleft()]): #인접 정점은 오름차순으로 방문
            if visited[f] == 0:
                count += 1
                visited[f] = count
                queue.append(f)

bfs(graph, r, visited) #실행
for i in range(1, len(visited)):
    print(visited[i])








