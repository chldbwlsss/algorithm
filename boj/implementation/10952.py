### A+B - 5 / 구현 ###
while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(str(a + b))
    else:
        break  #while문 탈출 잊지말자
