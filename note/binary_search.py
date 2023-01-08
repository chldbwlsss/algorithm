arr = [1, 2, 3, 8, 20, 24, 29]

#배열 안에서 원하는 숫자의 위치 찾기(인덱스 리턴)
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

print(binary_search2(arr, 24, 0, len(arr) - 1))

