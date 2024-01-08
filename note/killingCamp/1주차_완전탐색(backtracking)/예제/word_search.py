class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        def in_range(i, j):
            if i>=0 and i<n and j>=0 and j<m:
                return True
            return False

        def backtracking(i, j, w, visited): #w는 찾아야하는 철자의 인덱스
            if not visited[i][j] and board[i][j] == word[w]:
                if w == len(word) - 1:
                    return True
                visited[i][j] = True #방문처리
                flag = False
                for x, y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if in_range(i+x, j+y):
                        if backtracking(i+x, j+y, w+1, visited):
                            flag = True
                visited[i][j] = False
                return flag

        for i in range(n):
            for j in range(m):
                if backtracking(i, j, 0, visited):
                    return True
        return False






