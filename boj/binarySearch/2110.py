##공유기 설치
import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))
#집 좌표
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

start = 1 #가능한 최소 거리
end = home[-1] - home[0] #가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    #첫번쨰 집에는 무조건 설치한다고 가정
    value = home[0]
    count = 1
    #두번째 집부터 설치 시작
    for i in range(1, n):
        if home[i] >= value + mid:
            value = home[i]
            count += 1
    #공유기를 설치한 횟수가 주어진 수보다 많으면
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)
