### bfs ###
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
count = 0
visited = [[False] * m for _ in range(n)]  #방문처리
distance = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

#동서남북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0))  #시작점 ### bfs ###
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
count = 0
visited = [[False] * m for _ in range(n)]  #방문처리
distance = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

#동서남북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0))  #시작점 좌표 자체를 넣어줌
distance[0][0] = 1   #시작점부터 개수 카운팅

while queue:
    nowx, nowy = queue.popleft()
    for i in range(4):
        nx, ny = nowx + dx[i], nowy + dy[i]  #상하좌우
        if 0 <= nx < n and 0 <= ny < m:     #그래프 벗어나지 않고
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] += distance[nowx][nowy] + 1  #현재 카운팅 값에 +1
                visited[nx][ny] = True  #방문처리

#실행
print(distance[n-1][m-1])


#좌표 자체를 넣어줌
distance[0][0] = 1   #시작점부터 개수 카운팅

while queue:
    nowx, nowy = queue.popleft()
    for i in range(4):
        nx, ny = nowx + dx[i], nowy + dy[i]  #상하좌우
        if 0 <= nx < n and 0 <= ny < m:     #그래프 벗어나지 않고
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] += distance[nowx][nowy] + 1  #현재 카운팅 값에 +1
                visited[nx][ny] = True  #방문처리

#실행
print(distance[n-1][m-1])


