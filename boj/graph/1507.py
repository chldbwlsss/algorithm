### 궁금한 민호 ###
## 플로이드 워셜
import sys
input = sys.stdin.readline
n = int(input())
t = []
t_ = [[1] * n for i in range(n)]
result = 0

for i in range(n):
    t.append(list(map(int, input().split())))

def floyd():
    global result
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or j == k or i == k:
                    continue
                if t[i][j] == t[i][k] + t[k][j]:
                    t_[i][j] = 0
                elif t[i][j] > t[i][k] + t[k][j]:
                    result = -1
floyd()
if result != -1:
    for i in range(n):
        for j in range(i, n):
            if t_[i][j]:
                result += t[i][j]
print(result)





