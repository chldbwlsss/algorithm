#0:빈 칸, 1:벽, 2:바이러스
import sys
from collections import deque, Counter
from itertools import combinations
input = sys.stdin.readline

# n:세로크기, m:가로크기
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus, empty = [],[]
answer = 0

#빈칸, 바이러스 위치 저장
for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty.append([r,c])
        elif board[r][c] == 2:
            virus.append([r,c])

#유효한 범위 검사
def in_range(next_i, next_j):
    return 0 <= next_i < n and 0 <= next_j < m

def bfs():
    global answer
    tmp = [board[i][:] for i in range(n)] #board 쌍둥이 생성
    queue = deque(virus)

    #bfs를 통해 바이러스 전파
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c = r+dr, c+dc
            if in_range(next_r, next_c):
                # 바이러스 상하좌우에 있는 칸이 빈칸이면(0이면) 바이러스 전파
                if tmp[next_r][next_c] == 0:
                    tmp[next_r][next_c] == 2
                    queue.append((next_r,next_c))

    # 전파 완료 후 0, 1, 2 개수 세기
    count = Counter([]) # Counter -> 각 요소의 개수를 리턴
    for row in tmp:
        count += Counter(row)

    # 빈칸 개수를 통해 정답 갱신
    answer = max(answer, count[0]) #count[0]에서 0은 key임 (요소 0의 개수 리턴)
    return

# 새로운 벽 3개를 설치하는 경우의 수 -> 벽 설치 가능한 곳에 다 설치해보고 bfs() 돌리고 원복
for new_wall in combinations(empty, 3): # 3개의 원소로 이루어진 모든 조합을 생성하는 이터레이터를 반환
    row, col = [], [],
    for r, c in new_wall:
        row.append(r)
        col.append(c)
        if board[r][c] != 0:
            break
    else:
        for i in range(3):
            board[row[i]][col[i]] = 1
        bfs()
        for i in range(3):
            board[row[i]][col[i]] = 0

print(answer)