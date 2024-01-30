import heapq

INF = 1e9


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [INF] * (n + 1)


        graph = [[] for _ in range(n+1)]
        for time in times:
            u, v, w, = time
            graph[u].append((v, w))

        hq = []
        heapq.heappush(hq, (0, k))
        distance[k] = 0
        distance[0] = -1

        while hq:
            dist, v = heapq.heappop(hq)
            if distance[v] < dist:
                continue
            for next_v, cost in graph[v]:
                next_dist = dist + cost
                if next_dist < distance[next_v]:
                    distance[next_v] = next_dist
                    heapq.heappush(hq, (next_dist, next_v))

        if INF in distance:
            return -1

        return max(distance)
