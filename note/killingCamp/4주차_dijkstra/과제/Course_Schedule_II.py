# 위상정렬
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        result = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:    # 시작
                queue.append(i)

        while queue:
            v = queue.popleft()
            result.append(v)

            for n in graph[v]:
                indegree[n] -= 1

                if indegree[n] == 0:    # 방문 가능해짐
                    queue.append(n)

        if len(result) != numCourses:
            return []

        return result
