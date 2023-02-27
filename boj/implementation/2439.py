### 별 찍기 - 2 / 구현 ###
n = int(input())

for i in range(1, n + 1):
    star = "*" * i
    print(star.rjust(n)) #전체 n 중 오른쪽 정렬