### 플로이드 - 워셜 ###
import sys
n = int(input())    #노드
m = int(input())    #간선
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):  #본인~본인은 0으로
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):   #입력받은 각 간선에 대한 정보 담기
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()