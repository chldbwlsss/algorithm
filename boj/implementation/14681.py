### 사분면 고르기 / 구현 ###
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(int(1))
elif x > 0 and y < 0:
    print(int(4))
elif x < 0 and y > 0:
    print(int(2))
elif x < 0 and y < 0 :
    print(int(3))
