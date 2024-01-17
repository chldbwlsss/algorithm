from collections import deque


# 최단거리니까 출발지로부터 가까운부분부터 탐색해나간다 -> bfs
# 동서남북대각선 가능
# 결론은 depth + 1
# grid[0][0]부터 시작, 주변을 bfs로 보며 0이면 진행

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        if n == 1:
            return 1
        start = (0, 0)
        depth = 0
        visited = [[False for _ in range(n)] for _ in range(n)]
        dx = [0, 1, 0, -1, -1, 1, -1, 1]
        dy = [1, 0, -1, 0, 1, 1, -1, -1]
        queue = deque()
        queue.append((start, depth))
        visited[0][0] = True

        while queue:
            v, depth = queue.popleft()

            for i in range(8):
                nxt_x = v[0] + dx[i]
                nxt_y = v[1] + dy[i]
                if 0 <= nxt_x < n and 0 <= nxt_y < n and not visited[nxt_x][nxt_y] and grid[nxt_x][nxt_y] == 0:
                    queue.append(((nxt_x, nxt_y), depth + 1))
                    visited[nxt_x][nxt_y] = True

                if nxt_x == n - 1 and nxt_y == n - 1:
                    return depth + 2

        return -1