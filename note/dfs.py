#dfs는 스택과 관련이 있다.
n = 10

visited = [False] * n
graph = [[1, 2], [0, 3, 4], [0, 5], [1, 4], [1, 3], [2]]  #그림
def dfs(graph, v):  #방문하고 인접한 친구 찾기
    visited[v] = True
    graph[v]  #v친구들
    for f in graph[v]:
        if not visited[f]:
            dfs(graph, f)

