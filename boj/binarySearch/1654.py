##랜선 자르기
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

#몇센치로 자를건지 기준을 잡기 > 어떻게?
#기준값으로 잘랐을때 랜선 개수가 11개(n개)가 안나오면 기준값 줄이기(이진탐색으로)
def binary_search(arr, target, start, end):
    result = 0
    #start는 최소 1cm, end는 가장 긴 랜선
    while start <= end:
        #처음에는 중간을 pick으로
        pick = (start + end) // 2

        if can_cut_cable(target, pick, arr):
            # 자를 수 있으면 기록하기
            result = pick
            #그리고 더 길게 잘라봄
            start = pick + 1
        else: #개수가 안나오면 pick을 줄여봄
            end = pick - 1
    return result

#pick으로 자를수있는지 없는지(pick으로 잘라서 목표 랜선 개수가 나올수 있는지 없는지 확인하는 함수)
def can_cut_cable(n, pick, arr):
    count = 0  #랜선 개수
    for x in arr:
        count += x // pick

    return count >= n


print(binary_search(arr, n, 1, max(arr)))