### bfs or dfs ###
## 접근: 방문한곳은 0으로 바꿔서 다시 방문하지 않도록 함
n = int(input())
graph = [[0]*n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    line = input()
    for j, b in enumerate(line):
        graph[i][j] = int(b)

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):  #x, y는 현재 위치
    global cnt
    visited[x][y] = True #방문처리
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):  #상하좌우 보기(1있는지)
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

cnt = 0  #단지 수 카운팅
housing = []

#시작점이 안주어졌으니 graph[0][0]부터 찾아나감
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            housing.append(cnt)
            cnt = 0

#답 출력
housing.sort()
print(len(housing))
for i in housing:
    print(i)



