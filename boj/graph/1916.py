### 최소비용 구하기 ###
## 벨만포드

import sys
n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

start, end = map(int, input().split())

#함수 선언
def bellman_ford(edges, n):
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True

    return dist[end]

print(bellman_ford(edges, n))


