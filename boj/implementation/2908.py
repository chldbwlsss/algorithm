### 상수 ###
a, b = map(str, input().split())
a_reverse = a[::-1]
b_reverse = b[::-1]

print(max(a_reverse, b_reverse))