### 킹, 퀸, 룩, 비숍, 나이트, 폰 ###

cnt = [1, 1, 2, 2, 2, 8]
m = list(map(int, input().split()))
ans = [0, 0, 0, 0, 0, 0]

for i in range(len(m)):
    ans[i] = cnt[i] - m[i]

for item in ans:
    print(item, end=" ")
