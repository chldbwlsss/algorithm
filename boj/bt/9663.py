##N-Queen
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
column_set = set() #인덱스값
diagonal_set1 = set()
diagonal_set2 = set()
choose = []
count = 0

def queen(x):
    global count
    if len(choose) == n:
        count += 1
    for i in range(n):
        if i not in column_set and (x + i) not in diagonal_set1 and (x - i) not in diagonal_set2:
            choose.append((x, i))   #state 만들기
            column_set.add(i)
            diagonal_set1.add(x + i)
            diagonal_set2.add(x - i)

            queen(x + 1) #다음줄

            choose.pop()
            column_set.remove(i)
            diagonal_set1.remove(x + i)
            diagonal_set2.remove(x - i)

queen(0)
print(count)