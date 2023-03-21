### 최단경로 - 플로이드 워셜 ###
## 시간복잡도 : O(V^3)  => for문을 3중으로 하니까
## '거쳐 가는 노드'가 기준

INF = int(1e9) #무한
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)] #이차원 리스트 만들고 모든 값 무한으로 초기화

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0

for _ in range(m): #입력받은 각 간선에 대한 정보로 초기화
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):     #거쳐가는노드 k
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("infinity")
        else:
            print(graph[a][b])

