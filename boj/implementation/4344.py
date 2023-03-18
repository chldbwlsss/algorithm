### 평균은 넘겠지 ###
c = int(input())
total = 0
cnt = 0 #평균 이상인 학생 수

for _ in range(c):
    t = list(map(int, input().split()))
    for i in range(1, len(t)):
        total += t[i]
    avg = total/t[0]  #평균
    for i in range(1, len(t)):
        if t[i] > avg:
            cnt += 1
    per = (cnt/t[0])*100
    print("{:.3f}".format(per) + '%')
    total = 0
    cnt = 0
