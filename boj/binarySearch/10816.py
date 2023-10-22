##숫자 카드2
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

#이분탐색을 위한 정렬
sorted_n = sorted(n_arr)

def binary_search(arr, target, start, end):
    result = 0
    if start > end:
        return None
    elif start == end:
        if arr[start] == target:
            result += 1
        else:
            return 0
    else:
        mid = (start + end) // 2 #mid는 인덱스!
        if arr[mid] == target:
            result += 1
        elif arr[mid] > target:
            binary_search(arr, target, start, mid-1)
        else:
            binary_search(arr, target, mid+1, end)




# 수 세기
count = {}

for i in m_arr:
    binary_search(sorted_n, m_arr[i], 0, n-1)




#왼쪽 인덱스
# 타겟보다 작을때 > 오른쪽 탐색 (스타트 이동)
# 타겟보다 클때 > 왼쪽 탐색 (끝 이동)
# 타겟과 같을때 > 인덱스 저장 후 (왼쪽)  탐색

