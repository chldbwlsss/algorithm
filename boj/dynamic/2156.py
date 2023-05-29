## 포도주 시식
n = int(input())
wine = []
dp = [0] * n
for _ in range(n):
    wine.append(int(input()))

for i in range(n):
    if i == 0:
        dp[i] = wine[i]
    elif i == 1:
        dp[i] = wine[i-1] + wine[i]
    elif i == 2:
        dp[i] = max((wine[i-2] + wine[i-1]), (wine[i-2] + wine[i]), (wine[i-1] + wine[i]))
    else:
        dp[i] = max((dp[i - 2] + wine[i]), (dp[i - 3] + wine[i - 1] + wine[i]), dp[i - 1])

answer = dp[-1]
print(answer)

