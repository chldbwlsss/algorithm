# #수 찾기
n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

sorted_n = sorted(n_array)

def binary_search(arr, target, start, end):
    if start > end:
        return None
    elif start == end:
        if arr[start] == target:
            return start
        else:
            return None
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, end)
        else:
            return binary_search(arr, target, start, mid-1)


for i in m_array:
    idx = binary_search(sorted_n, i, 0, len(sorted_n) - 1)
    if idx == None:
        print(0)
    else:
        print(1)

# n = int(input())
# n_arr = list(map(int, input().split()))
# m = int(input())
# m_arr = list(map(int, input().split()))
#
# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# for x in m_arr:
#     result = binary_search(sorted(n_arr), x, 0, n - 1)
#     if result == None:
#         print(0)
#     else:
#         print(1)