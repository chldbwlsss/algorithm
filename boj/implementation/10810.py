### 공 넣기 ###
n, m = map(int, input().split())
bowl = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j + 1):
        bowl[l - 1] = k

for i in range(n):
    print(bowl[i], end=" ")