### 바구니 뒤집기 ###
n, m = map(int, input().split())
bowl = [i for i in range(1, n + 1)] # 1, 2, 3, ...

for _ in range(m):
    a, b = map(int, input().split())
    bowl = bowl[:a - 1] + bowl[a - 1:b][::-1] + bowl[b:]   #

for item in bowl:
    print(item, end=' ')

