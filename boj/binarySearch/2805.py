#나무 자르기
n, m = map(int, input().split())    #n:나무 수, m:목표 나무 길이
arr = list(map(int, input().split()))

def bin(arr, m, start, end):
    result = 0
    while start <= end:
        #처음에는 중간을 자름
        h = (start + end) // 2
        # 목표길이가 나오면 절단기 높이를 더 높여서 잘라볼거임
        if can_cut(h, arr, m):
            result = h
            start = h + 1
        #자를수없으면(목표치보다 모자르면)
        else:
            end = h - 1
    return result

#자를수있는지 없는지 확인하는 함수
def can_cut(h, arr, m): #m은 목표 나무 길이
    result = 0
    for k in arr:
        real = k - h
        if real > 0:
            result += real #나무길이 - 절단기 높이

    return result >= m

print(bin(arr, m, 0, max(arr)))


