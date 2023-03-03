### 문자열 반복 ###
t = int(input())

for i in range(t):
    r, s = input().split()
    answer = ""
    for item in str(s):
        answer += str(item) * int(r)
    print(answer)