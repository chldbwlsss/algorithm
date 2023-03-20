### 토마토 ###
## 3차원 배열
from collections import deque
import sys
m, n, h = map(int, input().split())
graph = []
queue = deque([])

# 우선, 익은 토마토 큐에 넣기
for i in range(h):
    tmp = []  #3차원 배열
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tmp)

#상하좌우앞뒤
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

#함수 선언
def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
                queue.append([a, b, c])
                graph[a][b][c] = graph[x][y][z] + 1
#함수 실행
bfs()
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)

