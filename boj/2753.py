### 윤년 / 구현 ###
year = int(input())

if (year%4 == 0 and not year%100 == 0) or year%400 == 0:
    print(1)
else:
    print(0)