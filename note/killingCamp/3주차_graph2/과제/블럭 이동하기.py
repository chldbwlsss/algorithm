from collections import deque


def get_next_position(pos, board):  # 이동 가능한 경우의 수 도출
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    (r1, c1), (r2, c2) = pos   # 현제 위치
    next_position_list = []

    # 상하좌우
    for i in range(4):
        next_r1, next_c1 = (r1 + dr[i], c1 + dc[i])
        next_r2, next_c2 = (r2 + dr[i], c2 + dc[i])
        if board[next_r1][next_c1] == 0 and board[next_r2][next_c2] == 0:        # 두칸 다 0이어야 갈수있음
            next_position_list.append(((next_r1, next_c1), (next_r2, next_c2)))     # 만족하면 갈수있따~

    # 가로일 때 회전
    if r1 == r2:
        # 위쪽이 비어있을 떄, 회전
        if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:   # 어쨌든 위 두칸이 0이어야 회전가능
            next_position_list.append(((r1, c1), (r1 - 1, c1)))
            # next_position_list.append(((r2, c2), (r2 - 1, c2))) # 여기 좀 다르게씀
            next_position_list.append(((r2 - 1, c2), (r2, c2)))
        # 아래쪽이 비어있을 때, 회전
        if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
            next_position_list.append(((r1, c1), (r1 + 1, c1)))
            # next_position_list.append(((r2, c2), (r2 + 1, c2),))    # 여기 좀 다르게씀
            next_position_list.append(((r2 + 1, c2), (r2, c2)))
    # 세로일 때 회전
    if c1 == c2:
        # 왼쪽이 비었을 때, 회전
        if board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
            # next_position_list.append(((r1, c1 - 1), (r1, c1))) # 여기 좀 다르게씀
            next_position_list.append(((r1, c1), (r1, c1 - 1)))
            next_position_list.append(((r2, c2 - 1), (r2, c2)))
        # 오른쪽이 비었을 때, 회전
        if board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:
            next_position_list.append(((r1, c1), (r1, c1 + 1)))
            # next_position_list.append(((r2, c2), (r2, c2 + 1)))       # 여기 좀 다르게씀
            next_position_list.append(((r2, c2 + 1), (r2, c2)))

    return next_position_list


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for r in range(n):
        for c in range(n):
            new_board[r + 1][c + 1] = new_board[r][c]   # 1부터 시작

    start_pos = ((1, 1), (1, 2))    # 처음 시작
    start_dist = 0
    queue = deque()
    queue.append((start_pos, start_dist))
    visited = set()     # 이 문제는 두 개의 좌표를 표시해야함 + 중복 제거
    visited.add(start_pos)  # 방문처리

    while queue:
        cur_position, cur_dist = queue.popleft()   # 지금 있는 곳

        # 두개 중 하나라도 목적지에 도달한 경우
        if (n, n) in cur_position:  # 참고 : cur_position 은 현재 ((1, 1), (1, 2)) 이런 형태!
            return cur_dist

        # 이동 가능한 경우를 뽑아서 방문하지 않았다면 방문
        for next_position in get_next_position(cur_position, new_board):
            if next_position not in visited:
                queue.append((next_position, cur_dist + 1))
                visited.add(next_position)
