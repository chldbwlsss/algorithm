### 이진탐색 ###
## 시간 복잡도: O(logN)
## 미리 정렬이 되어있어야 함
## 배열 안에서 원하는 숫자의 위치 찾기(인덱스 리턴)
arr = [1, 2, 3, 8, 20, 24, 29]
#left,right는 시작과 끝값의 인덱스
# 1.재귀
def binary_search2(arr, target, left, right):  #return : 원하는 숫자의 위치(인덱스)
    if left > right:
        return -1
    mid_idx = (left + right) // 2
    if arr[mid_idx] == target:
        return mid_idx
    elif arr[mid_idx] < target:
        left = mid_idx + 1
        return binary_search2(arr, target, left, right)
    else:
        right = mid_idx - 1
        return binary_search2(arr, target, left, right)

# 2.반복문
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None



