## 한번 기울일때, 벽('#') 끝까지 감
## 파란구슬까지 빠지면 안됨
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

answer = 0  # 0 : 불가, 1 : 가능
queue = deque()
visited = set()

# 구슬 위치 확인
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            rr, rc = r, c
        elif board[r][c] == "B":
            br, bc = r, c

queue.append([rr, rc, br, bc, 1])  # 구슬 위치 담기, level 담기
visited.add((rr, rc, br, bc))   # 방문처리하기 ** 이전과는 다르게 방문처리 한 곳 좌표를 넣어줌

# 구슬 움직이기 / 현재 좌표와 상하좌우 좌표를 받아서 구슬이 움직인 후의 위치를 반환해줌
def move(r, c, dr, dc):
    count = 0
    while board[r + dr][c + dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        count += 1
    return r, c, count


while queue:
    cur_rr, cur_rc, cur_br, cur_bc, level = queue.popleft()
    if level > 10:
        break
    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        next_rr, next_rc, r_count = move(cur_rr, cur_rc, dr, dc)
        next_br, next_bc, b_count = move(cur_br, cur_bc, dr, dc)
        # 파란 구슬이 구멍에 들어간 경우
        if board[next_br][next_bc] == 'O':
            continue
        # 중복 제거
        if (next_rr, next_rc, next_br, next_bc) in visited:
            continue
        # 빨간 구슬이 구멍에 들어간 경우 -> 성공
        if board[next_rr][next_rc] == 'O':
            answer = 1
            break
        # 두 구슬의 위치가 같은경우 더 멀리서 이동된 구슬을 이전 칸으로 이동시켜서 수정해야함
        if next_rr == next_br and next_rc == next_bc:
            if r_count > b_count:
                next_rr -= dr
                next_rc -= dc
            else:
                next_br -= dr
                next_bc -= dc
        queue.append([next_rr, next_rc, next_br, next_bc, level + 1])
        visited.add((next_rr, next_rc, next_br, next_bc))
    else:
        continue
    break

print(answer)