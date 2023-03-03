### 문자열 ###
n = int(input())
for _ in range(n):
    st = str(input())
    print(st[0] + st[-1:])