### A+B - 8 / 구현 ###
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #" + str(i) + ": " + str(a) + " + " + str(b) + " = " + str(a+b))