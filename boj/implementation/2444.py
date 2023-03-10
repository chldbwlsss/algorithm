### 별 찍기 ###
n = int(input())

for i in range(1, n+1):
    print(' '*(n-i) + '*'*i + '*'*(i-1))

for j in reversed(range(1, n)):
    print(' '*(n-j) + '*'*j + '*'*(j-1))