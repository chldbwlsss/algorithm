### 오븐 시계 / 구현 ###
h, m = map(int, input().split())
nt = int(input())

h += nt // 60
m += nt % 60

if m >= 60:
    h += 1
    m -= 60

if h >= 24:
    h -= 24

print(h, m)