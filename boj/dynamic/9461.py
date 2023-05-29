##파도반 수열
t = int(input())

arr = [0 for _ in range(101)]
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2
arr[5] = 2
def p(n):
    if arr[n] == 0:
        idx = 0
        for i in range(1, n+1):
            if arr[i] == 0:
                idx = i
                break
        for i in range(idx, n+1):
            arr[i] = arr[i-1] + arr[i-5]
    return arr[n]

for _ in range(t):
    result = p(int(input()))
    print(result)
