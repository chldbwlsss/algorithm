##N과 M (4)
n, m = map(int, input().split())
pool = [x for x in range(1, n+1)]
result = []
small = []

def bt(arr):
    if len(arr) == m:
        newarr = [x for x in arr]
        result.append(newarr)
    else:
        for y in pool:
            if 0 != len(arr):
                if y >= arr[-1]:
                    arr.append(y)
                    bt(arr)
                    arr.pop()
            else:
                arr.append(y)
                bt(arr)
                arr.pop()

bt(small)

for x in result:
    for y in x:
        print(y, end=" ")
    print()