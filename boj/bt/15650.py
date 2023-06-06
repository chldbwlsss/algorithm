#N과 M (2)
import copy
n, m = map(int, input().split())

pool = [x for x in range(1, n+1)]
result = []
small = []

def bt(small, depth):
    if depth == m:
        result.append(copy.deepcopy(small))
    else:
        for i in pool:
            if i not in small:
                if 0 != len(small):
                    if i > small[-1]:
                        # print(small[-1])
                        small.append(i)
                        bt(small, depth + 1)
                        small.pop()
                else:
                    # print(i)
                    small.append(i)
                    bt(small, depth + 1)
                    small.pop()

bt(small, 0)

for x in result:
    for y in x:
        print(y, end=" ")
    print()


