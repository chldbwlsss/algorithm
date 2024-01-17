from collections import deque
# grid에서 1인부분을 찾으면 그 부분을 bfs 탐색.
# 사방이 0이면, 섬!
class Solution:
    def numIslands(self, grid):
        island_cnt = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        #동서남북
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        queue = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    island_cnt += 1 #섬 하나 보장
                    visited[i][j] = True
                    queue.append((i, j))

                    while queue:
                        nx, ny = queue.popleft()
                        for x, y in zip(dx, dy):
                            nxt_idx_x = nx+x
                            nxt_idx_y = ny+y

                            if 0 <= nxt_idx_x < m and 0 <= nxt_idx_y < n and not visited[nxt_idx_x][nxt_idx_y] and grid[nxt_idx_x][nxt_idx_y] == '1':
                                visited[nxt_idx_x][nxt_idx_y] = True
                                queue.append((nxt_idx_x, nxt_idx_y))

        return island_cnt