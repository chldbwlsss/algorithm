from collections import deque
# b -> a
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                queue.append(v)

        while queue:
            v = queue.popleft()
            visited.append(v)

            for nodes in graph[v]:
                indegree[nodes] -= 1

                if indegree[nodes] == 0:
                    queue.append(nodes)

        for i in indegree:
            if i != 0:
                return False

        return True

