##N과 M (3)
n, m = map(int, input().split())

pool = [x for x in range(1, n + 1)]
result = []
small = []

def bt(arr):
    if len(arr) == m:
        newarr = [x for x in arr]
        result.append(newarr)
    else:
        for i in pool:
            arr.append(i)
            bt(arr)
            arr.pop()

bt(small)

for x in result:
    for y in x:
        print(y, end=" ")
    print()
