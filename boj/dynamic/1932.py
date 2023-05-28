n = int(input())
graph = []
arr = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, len(graph)):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] += graph[i - 1][j]
        elif j == i:
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i - 1][j], graph[i - 1][j - 1])


print(max(graph[n-1]))


