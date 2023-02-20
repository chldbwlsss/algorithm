import sys
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    now = list(map(int, sys.stdin.readline().split()))
    dest = list(map(int, sys.stdin.readline().split()))

    check = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    queue = deque()

    # 나이트가 이동 가능한 방향
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]


    def bfs():
        queue.append(now)
        visited[now[0]][now[1]]  #방문처리

        while queue:
            x, y = queue.popleft()

            if x == dest[0] and y == dest[1]:   #출발지와 목적지가 같으면 0 리턴
                return 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if visited[nx][ny] == False:
                    if nx == dest[0] and ny == dest[1]:  # 8개 방향중에 도착지와 같은 곳을 만나면
                        visited[nx][ny] = True
                        return check[x][y] + 1
                    else:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        check[nx][ny] = check[x][y] + 1
    answer = bfs()
    print(answer)