### 평균 ###
n = int(input())
gd = list(map(int, input().split()))
m = max(gd)

new_score = []
for score in gd:
    new_score.append(score/m * 100)

avg = sum(new_score) / n
print(avg)

