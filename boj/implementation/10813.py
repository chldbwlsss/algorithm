### 공 바꾸기 ###
n, m = map(int, input().split())
bowl = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    bowl[i - 1], bowl[j-1] = bowl[j-1], bowl[i - 1]

for b in bowl:
    print(b, end=" ")