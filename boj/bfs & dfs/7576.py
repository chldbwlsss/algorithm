### dfs ###
## 접근 : 1인 토마토가 모두 출발점이 된다 => 1인 토마토는 다 큐에 넣는다. (*실수 : 나는 0,0부터 시작함.. 바보,,,,,)
from collections import deque
# 상자 가로, 세로
m, n = map(int, input().split())
# 토마토s
graph = []
queue = deque([])

# 익은토마토는 큐에 넣어줘야지?
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        #토마토 꺼내서
        x, y = queue.popleft()
        #주변 봐봐
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #해당 좌표가 토마토상자 크기를 넘어가면 안되고, 토마토가 안익은채로 있어야됨
            if 0 <= nx <n and 0 <= ny < m and graph[nx][ny] == 0:
                #익히고 1 더해주면서 일 수 세어주기
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()
day = 0
for i in graph:
    for j in i:
        #전부 봤는데 익지못한 토마토가 있으면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    #다 익혔으면 최댓값이 정답
    day = max(day, max(i))
print(day - 1)


