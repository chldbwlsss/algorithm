### bfs(너비 우선 탐색)###
# 달력으로 기억하기
# 큐 안에 있는 원소: 해당 노드는 이미 방문했으나 그 인접 노드는 방문하지 않은
## 순서 ##
# 노드에 방문하기
# 방문한 노드를 큐에 넣기
# 큐에서 첫번째 원소를 뽑아 해당 노드의 인접 노드(친구들)를 방문 하기
from collections import deque
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        for f in graph[queue.popleft()]:
            if not visited[f]:
                visited[f] = True
                queue.append(f)
                